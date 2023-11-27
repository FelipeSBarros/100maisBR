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
  - `python manage.py runscript publish_album.py`
- [ ] O usuário **pode** dar nota a cada disco indicado (valor de 1 a 5), mas pode seguir sem votar ou, ainda indicar que não escutou;
- [X] Caso a página da coletânea não seja acessada pelo usuário por X dias, a indicação de discos é pausada.
- [ ] Um email é enviado para avisar que indicação de discos foi pausada;
- [ ] Cada coletanea tem um painel com estatísticas das notas datas, e comprarações das notas atribuidas entre os demais, permitindo identificar o gosto músical, década, etc;
- [ ] Possibilidade de criar uma coletânea coletiva, para que mais de uma pessoa possa acessar a *timeline* e dar nota ao mesmo disco;

**Alguns detalhes:**

Não é preciso *logar* para acessar a *timeline* de indicação de discos.
O e-mail será usado só para avisar: link para a pagina de *timeline*; Ações de pausa no processo de indicação de discos;


## Como colaborar:  

1. Clone o repositorio
2. Crie um virtual env com python
3. Ative seu virtual env
4. Instale as dependencias
5. Configure a instancia com  .env
6. Execute os testes
7. Crie um novo branch
8. Contribua
9. Faça um [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

```console
git clone git@github.com:FelipeSBarros/100maisBR.git
cd 100maisBR
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ./contrib/env-semple .env
python3 manage.py test 
git checkout -b new_branch
```

**Fazendo a primeira carga de dados de albums**:

```commandline
python manage.py runscript load_albums_to_db
```
