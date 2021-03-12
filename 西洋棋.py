class Chess:
    def __init__(self,name,ENname,id,CHchess,walk):
        self.ChessName = name
        self.ChessENname = ENname
        self.Chessid = id
        self.ChessCHchess = CHchess
        self.ChessWalk = walk
    def showInfo(self):
        print(self.ChessName,"\t",self.ChessENname,"\t",self.Chessid,"\t",self.ChessCHchess,"\t",self.ChessWalk,"\t")
       

x1=Chess("國王","King","001","帥","只能走一格")
x2=Chess("騎士","Knight","002","馬","走[日]字形")
x3=Chess("城堡","Rook","003","車","只能直走")
x1.showInfo()
x2.showInfo()
x3.showInfo()

