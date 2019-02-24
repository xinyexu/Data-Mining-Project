import numpy as np
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt


def find_problem_dates(t_bill, corporate_dates):
    """
    This function checks if two list of dates match.
    input variables: two lists containing string data
    """
    in_t_not_cor = []
    in_cor_not_t = []
    for i in corporate_dates:
        if i not in t_bill:
            in_cor_not_t.append(i)
    for i in t_bill:
        if i not in corporate_dates:
            in_t_not_cor.append(i)
    return in_t_not_cor, in_cor_not_t


# in_t_not_cor, in_cor_not_t = find_problem_dates(list(t_bill_daily["DATE"]),
#                                                list(corporate_daily["DATE"]))
"""Data Extraction"""
start_date = "1996-12-31"
end_date = "2019-01-22"
# below are urls of csv data
# the last line shows the overall range of provided data
# the date in the middle shows the part we extract
# be sure not to extract data that exceeds the range
# 1996-12-31 to 2019-01-21
# ----------------------------------------------------------------------------
# read url
# ----------------------------------------------------------------------------
tbill_10year_daily_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bg" \
                         "color=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23f" \
                         "fffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&t" \
                         "ts=12&width=748&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&s" \
                         "how_tooltip=yes&id=DGS10&scale=left&cosd" \
                         "=" + start_date + "&coed=" + end_date + "&" \
                                                                  "line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&" \
                                                                  "mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily&fam=avg&fgst=lin&fg" \
                                                                  "snd=2009-06-01&line_index=1&transformation=&vintage_date=2019-01-21&rev" \
                                                                  "ision_date=2019-01-21&nd=1962-01-02"

federal_funds_rate_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?" \
                     "bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23fffff" \
                     "f&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&widt" \
                     "h=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes" \
                     "&id=DEXUSEU&scale=left&cosd=1999-01-04&coed=2019-02-15&line_color=%234572a7&l" \
                     "ink_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=999" \
                     "99&mma=0&fml=a&fq=Daily&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&trans" \
                     "formation=lin&vintage_date=2019-02-23&revision_date=2019-02-23&nd=1999-01-04"

corporate3A_effective_yield_url = "https://fred.stlouisfed.org/graph/fredgra" \
                                  "ph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgc" \
                                  "olor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%2344444" \
                                  "4&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_ti" \
                                  "tles=yes&show_tooltip=yes&id=BAMLC0A1CAAAEY&scale=left&cosd" \
                                  "=" + start_date + "&coed=" + end_date + "&" \
                                                                           "line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&" \
                                                                           "mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily%2C%20Close&fam=avg&" \
                                                                           "fgst=lin&fgsnd=2009-06-01&line_index=1&transformation=lin&vintage_date=" \
                                                                           "2019-01-21&revision_date=2019-01-21&nd=1996-12-31"

sp500_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9" \
            "f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff" \
            "&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=1" \
            "2&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_" \
            "titles=yes&show_tooltip=yes&id=SP500&scale=left&cosd=2009-02-23" \
            "&coed=2019-02-22&line_color=%234572a7&link_values=false&line_st" \
            "yle=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&f" \
            "ml=a&fq=Daily&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&tr" \
            "ansformation=lin&vintage_date=2019-02-23&revision_date=2019-02-" \
            "23&nd=2009-02-23"

china_us_exchange_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=" \
                    "%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgc" \
                    "olor=%23ffffff&height=450&mode=fred&recession_bars=on&tx" \
                    "tcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=" \
                    "0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&" \
                    "id=DEXCHUS&scale=left&cosd=1981-01-02&coed=2019-02-15&li" \
                    "ne_color=%234572a7&link_values=false&line_style=solid&ma" \
                    "rk_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&" \
                    "fq=Daily&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&" \
                    "transformation=lin&vintage_date=2019-02-23&revision_date" \
                    "=2019-02-23&nd=1981-01-02"

vix_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&" \
          "chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&heigh" \
          "t=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&" \
          "width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&s" \
          "how_tooltip=yes&id=VIXCLS&scale=left&cosd=1990-01-02&coed=2019-02-" \
          "21&line_color=%234572a7&link_values=false&line_style=solid&mark_ty" \
          "pe=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily%2C%20C" \
          "lose&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&transformation" \
          "=lin&vintage_date=2019-02-23&revision_date=2019-02-23&nd=1990-01-02"

emerging_bonds_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor" \
                     "=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_b" \
                     "gcolor=%23ffffff&height=450&mode=fred&recession_bars=on" \
                     "&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&" \
                     "trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip" \
                     "=yes&id=BAMLEMCBPITRIV&scale=left&cosd=1998-12-31&coed=" \
                     "2019-02-21&line_color=%234572a7&link_values=false&line_" \
                     "style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=999" \
                     "99&mma=0&fml=a&fq=Daily%2C%20Close&fam=avg&fgst=lin&fgs" \
                     "nd=2009-06-01&line_index=1&transformation=lin&vintage_d" \
                     "ate=2019-02-23&revision_date=2019-02-23&nd=1998-12-31"

# ----------------------------------------------------------------------------
# convert url into dataframe
# ----------------------------------------------------------------------------
tbill_string_file = requests.get(tbill_10year_daily_url).content
t_bill_daily = pd.read_csv(io.StringIO(tbill_string_file.decode('utf-8')))

cor_3A_string_file = requests.get(corporate3A_effective_yield_url).content
corporate_daily = pd.read_csv(io.StringIO(cor_3A_string_file.decode('utf-8')))

sp500_string_file = requests.get(sp500_url).content
sp500_daily = pd.read_csv(io.StringIO(sp500_string_file.decode('utf-8')))

exchange_string_file = requests.get(china_us_exchange_url).content
exchange_daily = pd.read_csv(io.StringIO(exchange_string_file.decode('utf-8')))

vix_string_file = requests.get(vix_url).content
vix_daily = pd.read_csv(io.StringIO(vix_string_file.decode('utf-8')))


em_bonds_string_file = requests.get(emerging_bonds_url).content
em_bonds_daily = pd.read_csv(io.StringIO(em_bonds_string_file.decode('utf-8')))


fed_file = requests.get(federal_funds_rate_url).content
fed_rate = pd.read_csv(io.StringIO(fed_file.decode('utf-8')))


""" Data Cleaning and Merge"""
# ----------------------------------------------------------------------------
# convert date into same standard, set index, then merge
# ----------------------------------------------------------------------------
t_bill_daily["DATE"] = pd.to_datetime(t_bill_daily["DATE"])
corporate_daily["DATE"] = pd.to_datetime(corporate_daily["DATE"])
sp500_daily["DATE"] = pd.to_datetime(sp500_daily["DATE"])
exchange_daily["DATE"] = pd.to_datetime(exchange_daily["DATE"])
vix_daily["DATE"] = pd.to_datetime(vix_daily["DATE"])
em_bonds_daily["DATE"] = pd.to_datetime(em_bonds_daily["DATE"])
fed_rate["DATE"] = pd.to_datetime(fed_rate["DATE"])

t_bill_daily = t_bill_daily.set_index('DATE')
corporate_daily = corporate_daily.set_index('DATE')
sp500_daily = sp500_daily.set_index('DATE')
exchange_daily = exchange_daily.set_index('DATE')
vix_daily = vix_daily.set_index('DATE')
em_bonds_daily = em_bonds_daily.set_index('DATE')
fed_rate = fed_rate.set_index('DATE')

combined = pd.concat([t_bill_daily, corporate_daily, sp500_daily, exchange_daily,
                    vix_daily, em_bonds_daily, fed_rate], axis=1, join='inner')


