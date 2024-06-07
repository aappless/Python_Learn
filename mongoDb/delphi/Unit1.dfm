object Form1: TForm1
  Left = 1231
  Top = 243
  Width = 555
  Height = 383
  Caption = 'Form1'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object btn1: TBitBtn
    Left = 56
    Top = 64
    Width = 75
    Height = 25
    Caption = 'btn1'
    TabOrder = 0
    OnClick = btn1Click
  end
  object edt1: TEdit
    Left = 176
    Top = 64
    Width = 249
    Height = 21
    TabOrder = 1
    Text = 'edt1'
  end
  object mmo1: TMemo
    Left = 176
    Top = 88
    Width = 249
    Height = 193
    Lines.Strings = (
      'mmo1')
    TabOrder = 2
  end
  object btn2: TBitBtn
    Left = 56
    Top = 112
    Width = 75
    Height = 25
    Caption = 'btn2'
    TabOrder = 3
    OnClick = btn2Click
  end
  object btn3: TBitBtn
    Left = 64
    Top = 152
    Width = 75
    Height = 25
    Caption = 'btn3'
    TabOrder = 4
    OnClick = btn3Click
  end
  object idpclnt1: TIdUDPClient
    Port = 0
    Left = 432
    Top = 88
  end
end
