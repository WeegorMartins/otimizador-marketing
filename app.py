import json
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from otimizador import aloca_otimo, responde

st.set_page_config(page_title="Para onde mando o próximo real?", page_icon="💸", layout="wide")
st.title("💸 Para onde mando o próximo real de marketing?")
st.caption(
    "Marketing Mix Modeling bayesiano: mede o efeito causal de cada canal, modela "
    "retornos decrescentes e otimiza a alocação do orçamento. ⏳ Primeira carga ~30s."
)

with open("curvas_resposta.json") as f:
    curvas = json.load(f)

orcamento = st.slider("Orçamento total semanal (R$)", 5000, 60000, 20000, 1000)

aloc_otima, venda_otima = aloca_otimo(orcamento, curvas)

# Comparação: divisão igual (o que a maioria faz) vs alocação ótima
canais = list(curvas.keys())
igual = orcamento / len(canais)
venda_igual = sum(responde(igual, curvas[c]) for c in canais)

c1, c2, c3 = st.columns(3)
c1.metric("Vendas com alocação ótima", f"R$ {venda_otima:,.0f}")
c2.metric("Vendas dividindo igual", f"R$ {venda_igual:,.0f}")
c3.metric("Ganho da otimização", f"R$ {venda_otima - venda_igual:,.0f}",
          delta=f"{100*(venda_otima/venda_igual - 1):.1f}%")

fig = go.Figure()
fig.add_bar(x=canais, y=[aloc_otima[c] for c in canais], name="Alocação ótima")
fig.add_bar(x=canais, y=[igual]*len(canais), name="Divisão igual")
fig.update_layout(template="plotly_white", barmode="group",
                  title="Quanto investir em cada canal", yaxis_title="R$ por semana")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Curvas de resposta (por que dividir igual desperdiça dinheiro)")
fig2 = go.Figure()
for c in canais:
    fig2.add_scatter(x=curvas[c]["gasto"], y=curvas[c]["venda"], mode="lines", name=c)
fig2.update_layout(template="plotly_white", xaxis_title="Gasto no canal (R$)",
                   yaxis_title="Vendas previstas (R$)")
st.plotly_chart(fig2, use_container_width=True)
st.info("Cada canal satura em ritmo diferente. O otimizador para de investir num canal "
        "quando o próximo real renderia mais em outro. É isso que a divisão igual ignora.")