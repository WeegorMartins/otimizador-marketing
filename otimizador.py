import numpy as np
from scipy.optimize import minimize

def responde(gasto, curva):
    """Venda prevista para um gasto, interpolando a curva de resposta do canal."""
    return np.interp(gasto, curva["gasto"], curva["venda"])

def aloca_otimo(orcamento_total, curvas):
    """Distribui o orçamento entre canais para MAXIMIZAR vendas previstas.
    Cada canal satura (retorno decrescente), então a solução não é óbvia."""
    canais = list(curvas.keys())
    n = len(canais)

    def neg_vendas(x):  # minimizamos o negativo = maximizamos vendas
        return -sum(responde(x[i], curvas[c]) for i, c in enumerate(canais))

    restricao = {"type": "eq", "fun": lambda x: np.sum(x) - orcamento_total}
    limites = [(0, orcamento_total) for _ in range(n)]
    x0 = np.full(n, orcamento_total / n)  # chute inicial: divisão igual

    sol = minimize(neg_vendas, x0, method="SLSQP", bounds=limites, constraints=restricao)
    return dict(zip(canais, sol.x)), -sol.fun