import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Monitor de Producción TecNM", layout="wide")

st.title("📊 Panel de Control de Eficiencia (OEE)")
st.write("Cálculo de Disponibilidad, Rendimiento y Calidad en tiempo real.")

# --- Sidebar para entrada de datos ---
st.sidebar.header("Configuración de Turno")
tiempo_total = st.sidebar.number_input("Tiempo total de turno (min)", value=480)
paros = st.sidebar.number_input("Tiempo de paros/mantenimiento (min)", value=30)
meta_piezas = st.sidebar.number_input("Meta de piezas por hora", value=100)
producidas = st.sidebar.number_input("Total piezas producidas", value=700)
defectuosas = st.sidebar.number_input("Piezas defectuosas (Scrap)", value=15)

# --- Cálculos de Ingeniería ---
tiempo_operativo = tiempo_total - paros
disponibilidad = (tiempo_operativo / tiempo_total) * 100
rendimiento = (producidas / (meta_piezas * (tiempo_operativo / 60))) * 100
calidad = ((producidas - defectuosas) / producidas) * 100
oee = (disponibilidad/100 * rendimiento/100 * calidad/100) * 100

# --- Visualización de Indicadores (KPIs) ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Disponibilidad", f"{disponibilidad:.1f}%")
col2.metric("Rendimiento", f"{rendimiento:.1f}%")
col3.metric("Calidad", f"{calidad:.1f}%")
col4.metric("OEE TOTAL", f"{oee:.1f}%", delta=f"{oee-85:.1f}% vs Meta 85%")

# --- Gráfica de Pastel con Plotly ---
st.subheader("Análisis de Pérdidas")
df_grafica = pd.DataFrame({
    "Categoría": ["Disponibilidad", "Rendimiento", "Calidad"],
    "Porcentaje": [disponibilidad, rendimiento, calidad]
})

fig = px.bar(df_grafica, x="Categoría", y="Porcentaje", color="Categoría", range_y=[0,100])
st.plotly_chart(fig, use_container_width=True)

if oee >= 85:
    st.success("🚀 ¡Nivel de Clase Mundial! Sigue así, Ingeniero.")
elif oee >= 60:
    st.warning("⚠️ Rendimiento aceptable, pero hay fugas de tiempo.")
else:
    st.error("🚨 Revisar línea de producción. Eficiencia crítica.")
