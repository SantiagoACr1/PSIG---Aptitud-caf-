# Función de clasificación de aptitud según profundidad
def clasificar_profundidad(valor):
    if valor == "Profundo":
        return "A1"  # Aptitud Alta
    elif valor == "Moderadamente profundo":
        return "A2"  # Aptitud Media
    elif valor in ["Superficial", "Muy superficial"]:
        return "A3"  # Aptitud Baja
    else:
        return "N1" # No apto



# Función de clasificación de aptitud según textura
def clasificar_textura(valor):
    if valor in ["FAr", "FA", "FL", "F", "FArL"]:
        return "A1"  # Aptitud Alta
    elif valor in ["A", "ArA"]:
        return "A2"  # Aptitud Media
    elif valor == "Ar":
        return "A3"  # Aptitud Baja
    else:
        return "N1" # No apto



# Función de clasificación de aptitud según drenaje
def clasificar_drenaje(valor):
    if valor == "Bueno":
        return "A1"  # Aptitud Alta
    elif valor in ["Moderado", "Excesivo"]:
        return "A2"  # Aptitud Media
    elif valor == "Imperfecto":
        return "A3"  # Aptitud Baja
    else:
        return "N1" # No apto




# Función de clasificación de aptitud según temperatura
def clasificar_temperatura(valor):
    if 19 <= valor < 22:
        return "A1"  # Alta aptitud
    elif (16 <= valor < 19) or (22 <= valor < 23):
        return "A2"  # Media aptitud
    elif (15 <= valor < 16) or (23 <= valor <= 24):
        return "A3"  # Baja aptitud
    else:
        return "N1"  # No apto



# Función de clasificación de aptitud según precipitación
def clasificar_precipitacion(valor):
    if valor < 1400:
        return "A3"  # Baja aptitud
    elif 1400 <= valor <= 2900:
        return "A1"  # Alta aptitud
    elif valor > 2900:
        return "A2"  # Media aptitud
    else:
        return None  # Por si hay algún valor nulo




# Función de clasificación de aptitud según pendiente
def clasificar_pendiente(valor):
    if valor < 25:
        return "A1"  # Aptitud Alta
    elif valor <= 75:
        return "A2"  # Aptitud Media
    else:
        return "A3" # Aptitud Baja




# Función para clasificar según distancia a vías
def clasificar_distancia(dist):
    if 0.0 <= dist < 0.17:
        return "A1"  # Aptitud Alta: muy cerca a vías
    elif 0.17 <= dist < 1.14:
        return "A2"  # Aptitud Media
    elif 1.14 <= dist <= 17.26:
        return "A3"  # Aptitud Baja: lejos de vías
    else:
        return "N1"  # No apto o fuera de rango




# Función de clasificación de aptitud según distancia a estación
def clasificar_distancia_estacion(distancia):
    if distancia <= 2:
        return "A1"  # Aptitud Alta
    elif distancia <= 6:
        return "A2"  # Aptitud Media
    elif distancia <= 15:
        return "A3"  # Aptitud Baja
    else:
        return "N1"  # No apto



# Función para clasificar cada fila
def calcular_apt_final(row):
    # Si hay restricciones normativas
    if row["No_Apto_RUNAP"] == "si" or row["No_Apto_FA"] == "si":
        return "NA"
    
    # Si alguno de los criterios técnicos es "N1"
    if any(row[atrib] == "N1" for atrib in atributos_aptitud):
        return "NA"
    
    # Calcular la moda entre atributos técnicos
    valores = [row[atrib] for atrib in atributos_aptitud if row[atrib] in ["A1", "A2", "A3"]]
    modo = pd.Series(valores).mode()
    if not modo.empty:
        return modo.iloc[0]
    else:
        return np.nan

