import inflection

# Countries' name
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zealand",
162: "Philippines",
166: "Qatar",
184: "Singapore",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America"
}

def country_name(country_id):
    return COUNTRIES[country_id]

###-----------------------------------------------------------------------------------------###

# Category for price range
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

###-----------------------------------------------------------------------------------------###

# Colors' name
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

###-----------------------------------------------------------------------------------------###

# Dicionário de taxas de câmbio em relação ao Real (BRL)
taxas_cambio = {
    'Botswana Pula(P)': 0.40,       # 1 BWP = 0.40 BRL
    'Brazilian Real(R$)': 1.0,      # 1 BRL = 1 BRL
    'Dollar($)': 5.43,              # 1 USD = 5.43 BRL
    'Emirati Diram(AED)': 1.48,     # 1 AED = 1.48 BRL
    'Indian Rupees(Rs.)': 0.065,    # 1 INR = 0.0065 BRL
    'Indonesian Rupiah(IDR)': 0.00034, # 1 IDR = 0.00034 BRL
    'NewZealand($)': 3.33,          # 1 NZD = 3.33 BRL
    'Pounds(£)': 6.90,               # 1 GBP = 6.90 BRL
    'Qatari Rial(QR)': 1.49,        # 1 QAR = 1.49 BRL
    'Rand(R)': 0.30,                # 1 ZAR = 0.30 BRL
    'Sri Lankan Rupee(LKR)': 0.018, # 1 LKR = 0.018 BRL
    'Turkish Lira(TL)': 0.16        # 1 TRY = 0.16 BRL
}

def converter_para_brl(cambio):
    moeda = cambio['currency']
    taxa = taxas_cambio.get(moeda, 1)  # Pega a taxa de câmbio, ou 1 se não encontrar
    return cambio['average_cost_for_two'] * taxa

###-----------------------------------------------------------------------------------------###

# Rename the column names to have a pattern
def rename_columns(dataframe):
    df = dataframe.copy()
    # capitalize all first letters
    title = lambda x: inflection.titleize(x)
    # put all letters in lowercase and join them with undercore
    snakecase = lambda x: inflection.underscore(x)
    # remove space in string
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    # the map function applies a function, in this case the title function, to each element in cols_old
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

###-----------------------------------------------------------------------------------------###

