# Gerando imagens com Kmeans

Este é um projeto que utiliza a biblioteca OpenCV em Python para calcular o kmeans da imagem. Neste trabalho, irei demonstrar a utilização do método kmeans do opencv, 
afim de mostrar o passo a passo que o método faz para poder reconstruir a imagem original.

## Sobre o trabalho

- Disciplina: OP63I-CC8 - Processamento de Imagens e Reconhecimento de Padrões
- Turma: 2023/2 - 8° Período
- Professor: Pedro Luiz de Paula Filho

## Pré-requisitos e Instalação no Linux

### Python (versão recomendada: 3.11 ou superior)

A maioria das distribuições Linux já vem com o Python instalado. Para verificar se o Python está instalado, abra o terminal e digite:

`python3 --version`

Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu/Debian:

`
sudo apt-get update
sudo apt-get install python3
`

No Arch Linux:

`
sudo pacman -Sy python
`

### PyCharm (ou qualquer outra IDE de sua escolha)

Você pode baixar o PyCharm diretamente do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/) ou, se preferir, pode usar o gerenciador de pacotes da sua distribuição para instalar a versão Community:

#### Ubuntu/Debian:

`
sudo snap install pycharm-community --classic
`

#### Arch Linux:

`
sudo pacman -Sy pycharm-community
`

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes Python:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Pré-requisitos e Instalação no Windows

### Python (versão recomendada: 3.11 ou superior)

1. Baixe o instalador Python para Windows no site oficial (https://www.python.org/downloads/windows/).

2. Execute o instalador e marque a opção "Adicionar o Python X.Y ao PATH" durante a instalação, onde X.Y é a versão do Python (por exemplo, 3.11).

### PyCharm (ou qualquer outra IDE de sua escolha)

1. Baixe o instalador do PyCharm Community ou Professional do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/).

2. Execute o instalador e siga as instruções na tela.

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes de pacotes Python:

Abra o prompt de comando (cmd) e execute:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Executando o Projeto

1. Clone este repositório em seu sistema:

`
git clone https://github.com/seuusuario/python-opencv-trabalho.git
`

2. Abra o projeto no PyCharm (ou sua IDE preferida).

## Modo de Uso

1. **Carregue uma imagem:** utilize a o botão de carregar imagem na interface gráfica para poder carregar uma imagem a partir de algum diretório.

2. **Parâmetros do Kmeans:**

   - O primeiro parâmetro se refere a dimensão da imagem, aonde quanto menor a dimensão mais rápido e melhor será para o algoritmo kmeans convergir
   - O segundo parâmetro é referente ao número de cluster do algoritmo, sendo que K = 1 a imagem se tornará a média das cores de todos os pixels e 10 é o número máximo de cluster.

3. **Gerar Kmeans:**

   - Utilize o botão de gerar kmeans para iniciar o algortimo. As imagens do passo a passo serão salvas no arquivo /images/saved-images

4. **Visualiizar o Kmeans:**
   - Se deseja visualizar o resultado sem acessar os arquivos salvos, utilize o botão de visualizar o kmeans para ver os resultados.
   - Para sair da visualização e poder gerar novas imagens pressione a tecla `ESC`.
  
5. **Kmeans App em funcionamento**
   - Carregando a imagem
   ![Screenshot_20231024_125631](https://github.com/emanuelamaral/kmeans_app_image/assets/105809178/f6c5b9a0-cd78-40af-ad31-abd87d40e812)

   - Gerando o Kmeans para os valores dos parâmetros default
     ![Screenshot_20231024_125823](https://github.com/emanuelamaral/kmeans_app_image/assets/105809178/b8ddfcbc-b232-46e0-baba-5a3a61fc3ab4)



## Autores

- Amoz Emanuel

## Referências

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python.org](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

