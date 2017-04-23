# Created by yreis at 4/11/17
# language: pt
@criar_post @core
Funcionalidade: Criar post
  Como usuário da aplicação
  Quero criar post
  Para que possa me comunicar com outras áreas

@criar_post_simples
Cenário: Criar post
  Dado que o usuário está logado
  Quando compor um post no feed
  E postar
  Então ele verá o post no feed

@criar_post_com_mencao
Cenário: create post with mention
  Dado que o usuário está logado
  Quando compor um post no feed com menção
  E postar
  Então ele verá o post no feed com a menção
  E na ação de clique a menção deverá direcionar o usuário ao perfil do usuário mencionado
