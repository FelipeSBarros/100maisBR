# [100MaisBR](https://twitter.com/100maisBr)  

Projeto colaborativo de implementação de um sistema de inicação dos melhores discos brasileiros, inspirado no [1001albumsgenerator](https://1001albumsgenerator.com/).
Atualmente o projeto indica os discos por email e também pelo [twitter](https://twitter.com/100maisBr).

Funções:  
- [ ] Cada usuário cria um 'projeto';
- [ ] Cada projeto tem sua *timeline* de discos indicados;
- [ ] Caso a página do 'projeto' não seja acessada pelo usuário por X dias, a indicação de discos é pausada. Um email é enviado para avisar;
- [ ] O usuário **pode** dar nota a cada disco indicado (valor de 1 a 5), mas pode seguir sem votar ou, ainda indicar que não escutou;
- [ ] Cada 'projeto' tem um painel com informações e comprarções das notas atribuidas entre os demais, permitindo identificar o gosto músical, década, etc;
- [ ] Possibilidade de criar um 'projeto' coletivo, para que mais de uma pessoa acessará a *timeline* e poderá dar notas ao mesmo disco;

Alguns detalhes:
Não é preciso *logar* para acessar a *timeline* de indicação de discos.
O e-mail será usado só para avisar: link para a pagina de *timeline*; Ações de pausa no processo de indicação de discos;


## como desenvolver
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
cp contrib/env-semple .env
python manage test 
git checkout -b new_branch
```
