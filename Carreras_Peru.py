import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo Excel
file_path = 'U.xlsx'  # Cambia esto a la ruta de tu archivo Excel
df = pd.read_excel(file_path)

# Calcular la mediana del "Número de puestos solicitados"
mediana_puestos = df['Número de puestos solicitados'].median()

# Función para gráfico de barras agrupadas
def plot_barras_agrupadas(df):
    fig, ax = plt.subplots(figsize=(14, 8))  # Ajustar el tamaño de la figura
    bar_width = 0.2
    index = range(len(df))
    bar1 = ax.bar(index, df['Ingreso promedio'], bar_width, label='Ingreso promedio')
    bar2 = ax.bar([i + bar_width for i in index], df['Mínimo'], bar_width, label='Mínimo')
    bar3 = ax.bar([i + 2 * bar_width for i in index], df['Máximo'], bar_width, label='Máximo')
    ax.set_xlabel('Carrera')
    ax.set_ylabel('Ingreso (S/)')
    ax.set_title('Comparación de Ingresos por Carrera Universitaria')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(df['Carrera'], rotation=90)
    ax.legend()
    st.pyplot(fig)

# Función para gráfico de caja y bigote (box plot)
def plot_box_plot(df):
    df_long = pd.melt(df, id_vars=['Carrera'], value_vars=['Ingreso promedio', 'Mínimo', 'Máximo'],
                      var_name='Tipo de Ingreso', value_name='Valor')
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.boxplot(x='Tipo de Ingreso', y='Valor', data=df_long, ax=ax)
    ax.set_title('Distribución de Ingresos por Tipo de Ingreso')
    st.pyplot(fig)

# Función para gráfico de número de puestos solicitados vs ingreso promedio
def plot_puestos_vs_ingreso(df):
    fig, ax = plt.subplots(figsize=(20, 12))
    scatter = sns.scatterplot(x='Ingreso promedio', y='Número de puestos solicitados', 
                              hue='Carrera', data=df, s=100, legend=False, ax=ax)
    mediana_puestos = df['Número de puestos solicitados'].median()
    ax.axhline(mediana_puestos, color='r', linestyle='--', 
                label=f'Mediana Puestos: {mediana_puestos:.0f}')
    ax.set_xlabel('Ingreso Promedio', fontsize=12)
    ax.set_ylabel('Número de Puestos Solicitados', fontsize=12)
    ax.set_title('Número de Puestos Solicitados vs Ingreso Promedio', fontsize=16)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    for idx, row in df.iterrows():
        ax.annotate(row['Carrera'], 
                    (row['Ingreso promedio'], row['Número de puestos solicitados']),
                    xytext=(5, 5), textcoords='offset points', 
                    fontsize=8, alpha=0.7,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.5))
    y_max = df['Número de puestos solicitados'].max()
    ax.set_ylim(0, y_max * 1.1)
    ax.legend(loc='upper right', fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

# Aplicación Streamlit
st.title('Análisis de Ingresos y Puestos Solicitados por Carrera Universitaria')
st.write('Este análisis muestra la comparación de ingresos y la relación entre el número de puestos solicitados y el ingreso promedio para diversas carreras universitarias.')

plot_barras_agrupadas(df)
plot_box_plot(df)
plot_puestos_vs_ingreso(df)

# Leer el archivo Excel
file_path = 'T.xlsx'  # Cambia esto a la ruta de tu archivo Excel
df = pd.read_excel(file_path)

# Calcular la mediana del "Número de puestos solicitados"
mediana_puestos = df['Número de puestos solicitados'].median()

# Función para gráfico de barras agrupadas
def plot_barras_agrupadas(df):
    fig, ax = plt.subplots(figsize=(14, 8))  # Ajustar el tamaño de la figura
    bar_width = 0.2
    index = range(len(df))
    bar1 = ax.bar(index, df['Ingreso promedio'], bar_width, label='Ingreso promedio')
    bar2 = ax.bar([i + bar_width for i in index], df['Mínimo'], bar_width, label='Mínimo')
    bar3 = ax.bar([i + 2 * bar_width for i in index], df['Máximo'], bar_width, label='Máximo')
    ax.set_xlabel('Carrera')
    ax.set_ylabel('Ingreso (S/)')
    ax.set_title('Comparación de Ingresos por Carrera Técnica')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(df['Carrera'], rotation=90)
    ax.legend()
    st.pyplot(fig)

# Función para gráfico de caja y bigote (box plot)
def plot_box_plot(df):
    df_long = pd.melt(df, id_vars=['Carrera'], value_vars=['Ingreso promedio', 'Mínimo', 'Máximo'],
                      var_name='Tipo de Ingreso', value_name='Valor')
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.boxplot(x='Tipo de Ingreso', y='Valor', data=df_long, ax=ax)
    ax.set_title('Distribución de Ingresos por Tipo de Ingreso')
    st.pyplot(fig)

# Función para gráfico de número de puestos solicitados vs ingreso promedio
def plot_puestos_vs_ingreso(df):
    fig, ax = plt.subplots(figsize=(20, 12))
    scatter = sns.scatterplot(x='Ingreso promedio', y='Número de puestos solicitados', 
                              hue='Carrera', data=df, s=100, legend=False, ax=ax)
    mediana_puestos = df['Número de puestos solicitados'].median()
    ax.axhline(mediana_puestos, color='r', linestyle='--', 
                label=f'Mediana Puestos: {mediana_puestos:.0f}')
    ax.set_xlabel('Ingreso Promedio', fontsize=12)
    ax.set_ylabel('Número de Puestos Solicitados', fontsize=12)
    ax.set_title('Número de Puestos Solicitados vs Ingreso Promedio', fontsize=16)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    for idx, row in df.iterrows():
        ax.annotate(row['Carrera'], 
                    (row['Ingreso promedio'], row['Número de puestos solicitados']),
                    xytext=(5, 5), textcoords='offset points', 
                    fontsize=8, alpha=0.7,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.5))
    y_max = df['Número de puestos solicitados'].max()
    ax.set_ylim(0, y_max * 1.1)
    ax.legend(loc='upper right', fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

# Aplicación Streamlit
st.title('Análisis de Ingresos y Puestos Solicitados por Carrera Técnica')
st.write('Este análisis muestra la comparación de ingresos y la relación entre el número de puestos solicitados y el ingreso promedio para diversas carreras técnicas.')

plot_barras_agrupadas(df)
plot_box_plot(df)
plot_puestos_vs_ingreso(df)
