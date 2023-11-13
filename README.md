# web-scrapper-FII
Esse projeto faz raspagem de dados de Fundos Imobiliários, e aplica  estratégias de investimentos.

#### Para rodar esse projeto em sua máquina siga os passos abaixo:

* Realize o git clone do repositório 
`git clone https://github.com/claytoncampos/web-scrapper-FII.git`
</br>

* Instale as bibliotecas de pré req 
`pip install -r requirements.txt`
</br>

##### Esse projeto exemplifica as fases de processo de ETL ( Extract, Tranform e Load)

<B>(EXTRACT)</B>
Esse projeto consiste em fazer um web scrapping de dados do site <b>founds explorer</b>, esses dados serão disponibilizados na camada <b>Raw</b>. 
<br>
<B>(TRANSFORM)</B>
Posteriormente iremos tratar os dados, remover duplicidades, dados incorretos, realizar tipagens e fazer as devidas tranformações necessárias, após esse processo iremos disponibilizar esses dados na camada <b>Refined.</b>
<br>
<B>(LOAD)</B>
E por último iremos fazer a carga desses dados na camada <b>Trusted</b> pronto para consumo.


