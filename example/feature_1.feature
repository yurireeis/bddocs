# Created by yreis at 4/11/17
Feature: Create comment

Scenario: create comment
  Given user user is logged
  When he go to control panel
  Then will see an access denied message


Scenario: create comment with mention
  Given user user is logged
  When he go to control panel
  Then will see an access denied message