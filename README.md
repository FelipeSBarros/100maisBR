# [100MaisBR](https://twitter.com/100maisBr)  

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  

Projeto colaborativo de implementação de um sistema de indicação dos melhores discos brasileiros, inspirado no [1001albumsgenerator](https://1001albumsgenerator.com/).
Atualmente o projeto indica os discos por email e também pelo [twitter](https://twitter.com/100maisBr).

**Funções:**  

- [X] Base de dados com albums de música brasileira;
- [X] Cada album tem os artistas envolvidos na obra numa relação M-2-M;
- [X] Cada usuário cria um '~~projeto~~ coletânea(?)';
- [ ] Um e-mail de confirmação é enviado ao usuário com o link de sua coletânea;
- [x] A cada dia o usuário recebe uma indicação de disco em sua coletânea (*timeline*);
  - Função [criada](./scripts/publish_album.py), falta criar teste e edicionar um *cronjob* para executá-lo todos os dias;  
  - `python3 manage.py runscript publish_album`
- [ ] O usuário **pode** dar nota a cada disco indicado (valor de 1 a 5), mas pode seguir sem votar ou, ainda indicar que não escutou;
- [X] Caso a página da coletânea não seja acessada pelo usuário por X dias, a indicação de discos é pausada.
- [ ] Um email é enviado para avisar que indicação de discos foi pausada;
- [ ] Cada coletanea tem um painel com estatísticas das notas datas, e comprarações das notas atribuidas entre os demais, permitindo identificar o gosto músical, década, etc;
- [ ] Possibilidade de criar uma coletânea coletiva, para que mais de uma pessoa possa acessar a *timeline* e dar nota ao mesmo disco;

**Alguns detalhes:**

Não é preciso *logar* para acessar a *timeline* de indicação de discos.
O e-mail será usado só para avisar: link para a pagina de *timeline*; Ações de pausa no processo de indicação de discos;


## Testando o projeto:  

1. Clone o repositorio
1. Crie um virtual env com python
1. Ative seu virtual env
1. Instale as dependencias
1. Configure a instancia com [.env](./contrib/env-sample)
1. Execute os testes
1. Execute as migrações
1. Crie um super usuário
1. Faça a [carga de albums ao banco de dados](./scripts/load_albums_to_db.py)
1. Inicie o servidor
1. Acessar o site e crie uma nova coletânea
1. Faça a [publicação de um album](./scripts/publish_album.py)
1. Acesse a página da coletânea e veja o album publicado;
1. Crie um novo branch
1. Contribua
1. Faça um [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

```console
cd 100maisBR
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo -n "SECRET_KEY=">.env; python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())
' -n >> .env
python3 manage.py test
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runscript load_albums_to_db
python3 manage.py runserver
python3 manage.py runscript publish_album
git checkout -b new_branch
```

**Fazendo a primeira carga de dados de albums**:

```commandline
python manage.py runscript load_albums_to_db
```

**Realizando a publicação dos álbums nas coletâneas criadas**:

A ideia é que todos os dias o seguinte script seja executado, para que os álbums sejam publicados nas coletâneas criadas:
```commandline
python3 manage.py runscript publish_album
```
