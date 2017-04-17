# Created by yreis at 4/11/17
@criar_post @nao_implementado
Feature: Create post
# Enter feature description here
As a common user
I want to create post
So that I can communicate with other areas

@criar_post_simples @nao_implementado
Scenario: create post
  Given user is logged
  When he go to control panel
  When will see the people settings

@criar_post_com_mencao @nao_implementado
Scenario: create post with mention
  Given user is not logged
  When he go to control panel
  When will see an access denied message
