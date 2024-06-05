import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Função para capturar dados simulados de sensores
def capture_sensor_data():
    temperatura = round(random.uniform(20.0, 30.0), 2)  # Temperatura em graus Celsius
    ph = round(random.uniform(7.0, 8.5), 2)  # pH da água
    poluicao_level = round(random.uniform(0.0, 100.0), 2)  # Nível de poluição em ppm
    biodiversidade_indice = round(random.uniform(0.0, 1.0), 2)  # Índice de biodiversidade
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Captura o timestamp atual
    return (timestamp, temperatura, ph, poluicao_level, biodiversidade_indice)  # Retorna os dados como uma tupla

# Função para visualizar os dados armazenados
def display_data(data_list):
    print("Dados Capturados:")
    print("Timestamp\t\tTemperatura\tpH\tPoluição Level\tIndice Biodiversidade")
    for data in data_list:
        print(f"{data[0]}\t{data[1]}\t\t{data[2]}\t{data[3]}\t\t{data[4]}")  # Imprime os dados formatados

# Função para plotar os dados em gráficos de colunas
def plot_data(data_list):
    df = pd.DataFrame(data_list, columns=['Timestamp', 'Temperatura', 'pH', 'Poluição Level', 'Indice Biodiversidade'])
    df.set_index('Timestamp', inplace=True)  # Define a coluna 'Timestamp' como índice
    df.index = pd.to_datetime(df.index)  # Converte o índice para datetime

    # Cria um layout de 2x2 para os gráficos
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plota a temperatura
    df['Temperatura'].plot(kind='bar', ax=axs[0, 0], color='skyblue')
    axs[0, 0].set_title('Temperatura')
    axs[0, 0].set_xlabel('Timestamp')
    axs[0, 0].set_ylabel('Temperatura (°C)')

    # Plota o pH
    df['pH'].plot(kind='bar', ax=axs[0, 1], color='lightgreen')
    axs[0, 1].set_title('pH')
    axs[0, 1].set_xlabel('Timestamp')
    axs[0, 1].set_ylabel('pH')

    # Plota o nível de poluição
    df['Poluição Level'].plot(kind='bar', ax=axs[1, 0], color='salmon')
    axs[1, 0].set_title('Poluição Level')
    axs[1, 0].set_xlabel('Timestamp')
    axs[1, 0].set_ylabel('Poluição Level (ppm)')

    # Plota o índice de biodiversidade
    df['Indice Biodiversidade'].plot(kind='bar', ax=axs[1, 1], color='gold')
    axs[1, 1].set_title('Indice Biodiversidade')
    axs[1, 1].set_xlabel('Timestamp')
    axs[1, 1].set_ylabel('Indice Biodiversidade')

    plt.tight_layout()  # Ajusta o layout dos gráficos
    plt.show()  # Exibe os gráficos

# Captura de dados e armazenamento em listas
def main():
    sensor_data_list = []
    for _ in range(10):  # Captura de 10 conjuntos de dados
        data = capture_sensor_data()
        sensor_data_list.append(data)

    # Exibir os dados capturados
    display_data(sensor_data_list)

    print("|") #Separação

    data_list = []
    media_temp = 0
    media_ph1 = 0
    media_pol = 0
    media_biod = 0
    for data in  sensor_data_list:
        temp = data[1]
        ph1 = data[2]
        pol = data[3]
        biod = data[4]
        media_temp += temp
        media_ph1 += ph1
        media_pol += pol
        media_biod += biod
    
    # Calcula a média dos dados
    temp_media = media_temp / 10
    ph1_media = media_ph1 / 10
    pol_media = media_pol / 10
    biod_media = media_biod / 10

    # Exibe as médias e interpreta os resultados
    print("Média dos dados: ")
    if temp_media <= 10:
        print(f"Temperatura média é {temp_media} A temperatura está muito baixa")
    elif temp_media > 10 and temp_media <=27: 
        print(f"Temperatura média é {temp_media} A temperatura está normal")  
    elif temp_media > 27:
        print(f"Temperatura média é {temp_media} A temperatura está muito alta")

    if ph1_media > 4 :
        print(f"O ph médio é {ph1_media}  nivel do ph está baixo")
    elif ph1_media >= 4 and ph1_media <= 6: 
        print(f"O ph médio é {ph1_media}  nivel do ph está Normal ")
    elif ph1_media > 6:
        print(f"O ph médio é {ph1_media}  nivel do ph está muito alto")

    if pol_media <= 20 :
        print(f"A poluição média é  {pol_media}  nivel da poluição está baixa")
    elif pol_media > 20 :
        print(f"A poluição média é {pol_media}  nivel da poluição está alta")

    if biod_media < 0.3 :
        print(f"A biodiversidade média é {biod_media} A biodiversidade esta baixa ")
    elif biod_media > 0.3 :
        print(f"A biodiversidade média é {biod_media}  A biodiversidade esta alta")

    # Plotar os dados em gráficos de colunas
    plot_data(sensor_data_list)

# Execução do programa principal
if __name__ == "__main__":
    main()
