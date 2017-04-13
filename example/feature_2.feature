# Created by yreis at 4/11/17
Feature: Create post
# Enter feature description here
As a common user
I want to create post
So that I can communicate with other areas

Scenario: create post
  Given user is logged
  When he go to control panel
  When will see the people settings


Scenario: create post with mention
  Given user is not logged
  When he go to control panel
  When will see an access denied message