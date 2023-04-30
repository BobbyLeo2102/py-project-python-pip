import matplotlib.pyplot as plt  # de esta manera creamos el alias 'plt' para llamar a la libreria de una forma mas eficiente y simple.

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels,values)  #estamos indicando a python de hacer una grafica de barras
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
