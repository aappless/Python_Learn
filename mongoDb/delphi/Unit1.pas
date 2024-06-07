unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, IdBaseComponent, IdComponent, IdUDPBase, IdUDPClient, StdCtrls,
  Buttons;

type
  TForm1 = class(TForm)
    btn1: TBitBtn;
    edt1: TEdit;
    mmo1: TMemo;
    idpclnt1: TIdUDPClient;
    btn2: TBitBtn;
    btn3: TBitBtn;
    procedure btn1Click(Sender: TObject);
    procedure btn2Click(Sender: TObject);
    procedure btn3Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.btn1Click(Sender: TObject);
var
  Response: string;

  Buffer: array[0..1024] of Char;
  sText: string;
  iLen: integer;
begin
  ZeroMemory(@Buffer, sizeof(Buffer));
 sText:=  edt1.Text;
  StrPCopy(Buffer,sText);
  iLen := Length(sText);

  idpclnt1.Host := 'localhost';
  idpclnt1.Port := 12345;




  try
    // 發送消息到服務器
  //  idpclnt1.Send(edt1.Text);

      idpclnt1.SendBuffer(Buffer,iLen);
    // 接收服務器的回應
    Response := idpclnt1.ReceiveString(5000); // 等待 5 秒
    if Response <> '' then
      mmo1.Lines.Add('Received: ' + Response)
    else
      mmo1.Lines.Add('No response received');
  except
    //連線失數
    on E: Exception do
      mmo1.Lines.Add('Error: ' + E.Message);
  end;
end;


procedure TForm1.btn2Click(Sender: TObject);
var
  Response: string;
begin
     idpclnt1.Host := 'localhost';
  idpclnt1.Port := 12345;
  try
    // 發送消息到服務器
    idpclnt1.Send(edt1.Text);
     // idpclnt1.SendBuffer(Buffer,iLen);
    // 接收服務器的回應
    Response := idpclnt1.ReceiveString(5000); // 等待 5 秒
    if Response <> '' then
      mmo1.Lines.Add('Received: ' + Response)
    else
      mmo1.Lines.Add('No response received');
  except
    on E: Exception do
      mmo1.Lines.Add('Error: ' + E.Message);
  end;
end;

procedure TForm1.btn3Click(Sender: TObject);
var
  Response: string;
  StartTick, Elapsed: Cardinal;
begin
  idpclnt1.Host := 'localhost';
  idpclnt1.Port := 12345;
  try
    // 發送消息到服務器
    idpclnt1.Send(edt1.Text);

    StartTick := GetTickCount;
    Elapsed := 0;

    // 連續接收多個回應，直到超時
    while Elapsed < 3000 do // 等待總共 5 秒
    begin
      try
        Response := idpclnt1.ReceiveString(1000); // 每次等待 1 秒
        if Response <> '' then
          mmo1.Lines.Add('Received: ' + Response)
        else
          mmo1.Lines.Add('No response received');

        Elapsed := GetTickCount - StartTick;
      except
        on E: Exception do
        begin
          mmo1.Lines.Add('Error: ' + E.Message);
          Exit;
        end;
      end;
    end;

  except
    on E: Exception do
      mmo1.Lines.Add('Error: ' + E.Message);
  end;

end;

end.

