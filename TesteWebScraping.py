# Python code
import urllib
import urllib2
import requests
 
url = 'http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/padrao_tiss_componente_organizacional_201902.pdf'

 
print "Baixando o componente organizacional"
urllib.urlretrieve(url, "padrao_tiss_componente_organizacional_201902.pdf")
 
