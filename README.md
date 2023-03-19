# image-compression-wav

# Compressão de Imagens usando Transformada Wavelet

Este repositório contém uma implementação em Python de compressão de imagens usando transformada wavelet. O algoritmo é configurável, permitindo que o usuário escolha o tipo de wavelet, o nível de compressão e o tamanho máximo da imagem.

## Instalação

1. Clone este repositório:
```
git clone https://https://github.com/lucenfort/image-compression-wav.git
```

2. Instale as dependências necessárias:
```
pip install -r requirements.txt
```


## Uso

### Comprimindo uma única imagem

```python
from compressao_de_imagens_com_wavelet import comprimir_imagem

imagem_comprimida = comprimir_imagem('caminho/para/imagem.jpg', wavelet='db2', nivel=2, tamanho_maximo=512)
```

### Comprimindo um diretório de imagens

```python
from compressao_de_imagens_com_wavelet import comprimir_imagens_em_dir

comprimir_imagens_em_dir('caminho/para/imagens', 'caminho/para/imagens_comprimidas', wavelet='haar', nivel=3, tamanho_maximo=1024)
```
