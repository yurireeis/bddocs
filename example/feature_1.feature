# Created by yreis at 4/11/17
@criar_comentario
Feature: Create comment

@criar_comentario_simples @core
Scenario: create comment
  Given user user is logged
  When he go to control panel
  Then will see an access denied message

@criar_comentario_com_mencao
Scenario: create comment with mention
  Given user user is logged
  When he go to control panel
  Then will see an access denied message
