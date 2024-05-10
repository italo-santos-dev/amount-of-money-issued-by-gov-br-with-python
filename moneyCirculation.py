import pandas as pd
import matplotlib.pyplot as plt
from bcb import DinheiroCirculacao

em = DinheiroCirculacao()

ep = em.get_endpoint('informacoes_diarias')

dados = ep.query().collect()

df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))
plt.plot(df['Data'], df['Quantidade'], marker='o', linestyle='-')

plt.title('Quantidade de Notas Emitidas pelo Governo Brasileiro ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Quantidade de Notas Emitidas')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()