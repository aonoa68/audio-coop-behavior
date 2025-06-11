import pygame, sys, pygame.mixer, time, glob, wx
from pygame.locals import *
from random import shuffle
import numpy as np


def main():
    (w,h) = (1500,1000) 
    SCR_RECT=Rect(0,0,w,h)  # 画面サイズ
    pygame.init()       # pygame初期化
	
    x = glob.glob("audio\*.wav") #audioの中のwavをリスト化
    y = glob.glob("faceshuffle\*.png") #faceshuffleの中の画像pngをリスト化
    kansai = [x[0],y[1]] #関西の音声と画像
    kagoshi = [x[1],y[3]] #鹿児島の音声と画像
    tarui = [x[2],y[0]] #垂井の音声と画像
    tokyo = [x[3],y[2]] #東京の音声と画像
    
    com_T_K = tokyo+kansai #東京ー関西の組み合わせ
    com_T_Tr = tokyo+tarui #
    com_T_N = kagoshi+tokyo #
    com_K_Tr = kansai+tarui #
    com_K_N = kagoshi+kansai #
    com_Tr_N = tarui+ kagoshi
    
	
    M=[com_T_K,com_T_Tr,com_T_N,com_K_Tr,com_K_N,com_Tr_N]
    shuffle(M)
    sys.stdout =open('list.txt','a')
    print(M)
	
	#shuffle(x) #リストをシャッフル
    #shuffle(y)
    
    pygame.mixer.init(frequency = 44100)    # 初期設定
    #pygame.display.set_mode(SCR_RECT.size, FULLSCREEN)  # 画面設定=display Surfaceを作成, pygame.display.set_mode(resolution=(0,0), flags=0, depth=0), resolution=幅と高さ。flags=追加で指定。depth=色を描写
    pygame.display.set_mode(SCR_RECT.size, 0)  # 画面設定=display Surfaceを作成, pygame.display.set_mode(resolution=(0,0), flags=0, depth=0), resolution=幅と高さ。flags=追加で指定。depth=色を描写
    pygame.display.set_caption("実験") #メニューバの表示名
    screen = pygame.display.get_surface() #作成済みのdisplay surfaceの情報を取得

    # テキスト入力
    input_box = pygame.Rect(50+10, 740, 100, 50)
    color_inactive = pygame.Color('yellow') #黄色であればアクティブでない
    color_active = pygame.Color('white') #白であればアクティブ
    color = color_inactive #color_inactive(黄)をcolorにいれる。#初期状態
    active = False
    text = ''
    done = False
    clock = pygame.time.Clock()
	
	#色の定義
    red = (200,0,0) #色の指定
    bright_red = (255,0,0)
    White = (255,255,255)
    black = (0,0,0)
    font = pygame.font.Font("ipag.ttf", 100)#フォントの指定
    font2 = pygame.font.Font("ipag.ttf", 40)#フォントの指定
    font3 = pygame.font.Font("ipag.ttf", 20)#フォントの指定
    
    lf = 375 #左の画像の中心座標x
    rt = 1125 #右の画像の中心座標x
    imageh = 200
    lf_m = 350 #左の人の口の図形の座標x
    rt_m = 1100 #右の人の口の図形の座標x
    m_y = 225 #人の口の図形の座標y
    m_c_h = 10 #閉じた口の図形の高さ
    m_o_h = 20 #開いた口の図形の高さ
    m_w = 50 #口の図形の長さ
    icon_w = 100 #Next, backボタンの長さ
    icon_h = 50 #Next, backボタンの高さ
    icon_x_n = 1400 #Nextのボタンの座標x
    icon_y_n = 900 #Nextのボタンの座標y
    icon_x_b = 0 #Backのボタンの座標x
    icon_y_b = 900 #Backのボタンの座標y
    	

    #bg = pygame.image.load("screen.png").convert_alpha()    # 背景画像の取得
    #rect_bg = bg.get_rect() #画像サイズの取得？
	
    k = 0; l = 6 #繰り返しの回数の設定(6パターン)

    while k < l:
        pygame.display.update()             # 画面更新
        pygame.time.wait(100)                # 更新時間間隔（ちょっとしくみがよく分からない）
        screen.fill((255, 255, 255, 0))          # 画面の背景色
        #screen.blit(bg, rect_bg)            # 背景画像の描画
        player = pygame.image.load(M[k][1]).convert_alpha()    # プレイヤー画像の取得
        #rect_player = player.get_rect()
        #rect_player.center = (300, 282)
        t_player= pygame.transform.scale(player, (300,282))
        rect_t_player = t_player.get_rect()
        rect_t_player.center = (lf, imageh)

        player2 = pygame.image.load(M[k][3]).convert_alpha()    # プレイヤー画像の取得2
        t_player2= pygame.transform.scale(player2, (300,282))
        rect_t_player2 = t_player2.get_rect()
        #rect_player2 = player2.get_rect()
        rect_t_player2.center = (rt,imageh)
        
        screen.blit(t_player, rect_t_player)    # プレイヤー画像の描画
        screen.blit(t_player2, rect_t_player2)    # プレイヤー画像の描画
        mouseclose1 = pygame.draw.rect(screen,red,Rect(lf_m,m_y,m_w,m_c_h))    # 左の人の口となる四角形を描画(閉じた口
        mouseclose2 = pygame.draw.rect(screen,red,Rect(rt_m,m_y,m_w,m_c_h))    # 右の人の口となる四角形を描画(閉じた口)
        
        tw = pygame.draw.rect(screen, (255, 234, 236), Rect(50,400,1400,580)) #テキストウィンドウの表示
        tw_moji = font2.render("どちらの声の人に2万円のうちいくらを投資したいですか。…(1)", True, (0,0,0))
        tw_moji2 = font3.render("このとき、あなたが選ばなかった方の人は1円も受け取れません。", True, (0,0,0))
        tw_moji3 = font2.render("その人に2万円からいくら投資しますか？…(2)", True, (0,0,0))
        
        #AかBかクリックで選ぶためのボタン
        pygame.draw.rect(screen, White, Rect(lf-100, 500, 200, 200))
        pygame.draw.rect(screen, White, Rect(rt-100, 500, 200, 200))	
        textAd = font.render("A", True, (0,0,0))   # 描画する文字列の設定
        screen.blit(textAd, [lf-25, 500+50])# 文字列の表示位置
        textBd = font.render("B", True, (0,0,0))   # 描画する文字列の設定
        screen.blit(textBd, [rt-25, 500+50])# 文字列の表示位置
        
		#値段の入力
        #クリック用の図形
        pygame.draw.rect(screen, red, Rect(50+10, 740, 100, 50))
        
		
        screen.blit(tw_moji, [50+10, 420])# 文字列の表示位置
        screen.blit(tw_moji2, [50+10, 460])# 文字列の表示位置
        screen.blit(tw_moji3, [50+10, 700])# 文字列の表示位置
        textA = font.render("A", True, (0,0,0))   # 描画する文字列の設定
        screen.blit(textA, [lf+10, 100])# 文字列の表示位置
        textB = font.render("B", True, (0,0,0))   # 描画する文字列の設定
        screen.blit(textB, [rt+10, 100])# 文字列の表示位置
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen,black,Rect(icon_x_n,icon_y_n,icon_w,icon_h)) #Nextボタン
        pygame.draw.rect(screen,black,Rect(icon_x_b,icon_y_b,icon_w,icon_h)) #Backボタン
        textN = font2.render('Next', True, (255,255,255))   # Nextボタンの文字
        screen.blit(textN, [icon_x_n, icon_y_n])# 文字列の表示位置
        textB = font2.render('Back', True, (255,255,255))   # Backボタンの文字
        screen.blit(textB, [icon_x_b, icon_y_b])# 文字列の表示位置
        text_k = font2.render(str(k+1), True, (0,0,0))   # 課題の連番描画する文字列の設定
        screen.blit(text_k, [10, 10])# 文字列の表示位置

        if lf_m+m_w > mouse[0] > lf_m and m_y+m_o_h > mouse[1] > m_y:#
            mouseopen1 = pygame.draw.ellipse(screen, bright_red,Rect(lf_m,m_y,m_w,m_o_h))	#左の人の開いた口
            if click[0]:
                print('左画像クリック時','k=',k,'m=',l)
                print(M[k][1])
                pygame.mixer.music.load(M[k][0])     # 音楽ファイルの読み込み
                pygame.mixer.music.play()             # 音楽の再生回数(1回再生)
                print('time',pygame.time.get_ticks())
                #pygame.mixer.music.stop()

				
        if rt_m+m_w > mouse[0] > rt_m and m_y+m_o_h > mouse[1] > m_y:
            mouseopen2 = pygame.draw.ellipse(screen, bright_red,Rect(rt_m,m_y,m_w,m_o_h))	#右の人の開いた口
            if click[0]:
                print ('右画像クリック時','k=',k,'m=',l)
                pygame.mixer.music.load(M[k][2])     # 音楽ファイルの読み込み
                pygame.mixer.music.play()             # 音楽の再生回数(1回再生)
                print('time',pygame.time.get_ticks())
                #pygame.mixer.music.stop()
				
        if lf-100 + 200 > mouse[0] > lf-100 and 500 + 200 > mouse[1] > 500: #A側の四角をマウスオーバーし、クリックしたとき
            pygame.draw.rect(screen, bright_red, Rect(lf-100, 500, 200, 200))
            if click[0]:
                print ('Aを選択','k=',k,'m=',l,'M=',M[k][0])

            
        if rt-100 + 200 > mouse[0] > rt-100 and 500 + 200 > mouse[1] > 500: #B側の四角をマウスオーバーし、クリックしたとき
            pygame.draw.rect(screen, bright_red, Rect(rt-100, 500, 200, 200))
            if click[0]:
                print ('Bを選択','k=',k,'m=',l,'M=',M[k][2])
				
        if 50+10 + 100 > mouse[0] > 50+10 and 740 + 50 > mouse[1] > 740: #値段入力のためのアイコンをマウスオーバーしたとき
            if click[0]:
                pygame.draw.rect(screen, White, Rect(input_box))
                while not done: #偽ではないときすなわち真のとき
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_F12:
                                done = True #ループを抜ける
                        if event.type == pygame.MOUSEBUTTONDOWN:# If the user clicked on the input_box rect.
                            if input_box.collidepoint(event.pos):#test if a point is inside a rectangle
                                active = not active #「偽ではない」をactiveにいれる。→アイコンが白くなる。
                            else:
                                active = False #それいがいは偽→アイコンが黄色くなる。
                            # Change the current color of the input box.
                            color = color_active if active else color_inactive #もし真ならcolor_activeをcolorにいれ、それ以外であれば、color_inactiveをcolorに入れる
                        if event.type == pygame.KEYDOWN:
                            if active:
                                if event.key == pygame.K_RETURN: #リターンキーを押したら
                                    print(text) #textをプリントする
                                    text = '' #textの内容は上記の''であり、ユーザーの入力するもの
                                elif event.key == pygame.K_BACKSPACE: #バックスペースキーを押したら
                                    text = text[:-1] #文字を消す
                                else:
                                    text += event.unicode #
									
                    txt_surface = font2.render(text, True, (0,0,0))				
                    pygame.draw.rect(screen,color, input_box,4) #図形を書く
                    screen.blit(txt_surface, (50+10, 740)) #文字列の表示位置
					
                    pygame.display.flip()
                    clock.tick(30)
				
        if icon_x_b+icon_w > mouse[0] > icon_x_b and icon_y_b+icon_h > mouse[1] > icon_y_b: #前の画面へ移動
            pygame.draw.rect(screen,red,Rect(icon_x_b,icon_y_b,icon_w,icon_h))
            screen.blit(textB, [icon_x_b, icon_y_b])# 文字列”Back”の表示位置
            textB = font2.render('Back', True, White)   # 描画する文字列の設定
            if click[0]: 
                print('Backクリック時','k=',k,'m=',l)
                k = k - 1
		
        if icon_x_n+icon_w > mouse[0] > icon_x_n and icon_y_n+icon_h > mouse[1] > icon_y_n: #次の2音声へ移動
            pygame.draw.rect(screen,red,Rect(icon_x_n,icon_y_n,icon_w,icon_h))
            screen.blit(textN, [icon_x_n, icon_y_n])# 文字列"Next"の表示位置
            textN = font2.render('Next', True, White)   # 描画する文字列の設定
            if click[0]: 
                print('Nextクリック時','k=',k,'m=',l)
                			
                k = k + 1
		
        for event in pygame.event.get():
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
                pygame.mixer()
            if event.type == KEYDOWN:  #キーを押したとき
			
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    pygame.mixer()				#ESCキーなら
					
    #else
            

if __name__ == "__main__":
    main()
    pg.init()
    pg.quit()