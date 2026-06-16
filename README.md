# 💸 Para onde mando o próximo real de marketing?

> Marketing Mix Modeling bayesiano que mede o ROI causal de cada canal de mídia,
> modela retornos decrescentes e otimiza a alocação do orçamento, com incerteza.

**🔗 [Teste ao vivo aqui](https://huggingface.co/spaces/Weegor/otimizador-marketing)**

## Por que este projeto é diferente
1. **Inferência bayesiana, não regressão ingênua.** Cada efeito vem com intervalo de
   credibilidade. Modela adstock (efeito que perdura) e saturação (retorno decrescente).
2. **Validado contra ground-truth.** Gerei dados com ROIs conhecidos e provei que o
   modelo os recupera antes de confiar nas estimativas.
3. **Termina em decisão, não em gráfico.** Um otimizador aloca o orçamento entre canais
   para maximizar vendas, e mostra o ganho sobre a divisão igual.

## Por que importa agora
Com o fim dos cookies e mudanças de privacidade, o rastreamento individual quebrou e o
MMM virou o padrão de medição de marketing, usando dados agregados que respeitam privacidade.

## Stack (100% gratuita)
PyMC-Marketing · PyMC · SciPy · Python · Streamlit · Plotly · Docker · Hugging Face

## Limitações
- Dados simulados com ground-truth (escolha deliberada para validar recuperação de ROI)
- Em produção, exige calibração com experimentos e dados reais de mídia e vendas
