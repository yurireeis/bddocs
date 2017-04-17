# Created by yreis at 4/11/17
@criar_comentario @nao_implementado
Feature: Create comment

@criar_comentario_simples @nao_implementado
Scenario: create comment
  Given user user is logged
  When he go to control panel
  Then will see an access denied message

@criar_comentario_com_mencao @nao_implementado
Scenario: create comment with mention
  Given user user is logged
  When he go to control panel
  Then will see an access denied message
