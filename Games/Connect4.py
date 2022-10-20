#This is the Main Project Code

def CreateCursorAndConnection():  
    def check_db_exists():
        
        if mycon is None:
            print("Error in connection, please retry.")
            return False
        
        else:
            try:
                table_create = 'create table UserData(pName varchar(30) primary key, pPass varchar(30) not null, pTotal int default 0, pWins int default 0, pLosses int default 0, pDraws int default 0);'
                cursor.execute(table_create)
                cursor.commit()
                print('Table "UserData" successfully created!')
                
            
            except:
                print('Error while creating table. Table may already exist.')
                time.sleep(5)
                os.system('cls')
        
    try:
        mycon = SQL.connect('connect4.db') 
        cursor = mycon.cursor()
        check_db_exists()
        return cursor, mycon
       
    except SQL.Error as e:
        print(e)
        print('Unexpected ERROR ecountered! \nPlease check system software for compatability.')
        time.sleep(10)
        return None, None

def CloseCursorAndConnection(cursor_obj, connection_obj):
    try:
        cursor_obj.close()
        connection_obj.close()
    except: pass

def SelectAllPlayerStats():
    cursor_obj, connection_obj = CreateCursorAndConnection()
    
    select_all_stats = "select pName as 'Player', pTotal as 'Games Played', pWins as 'Wins', pLosses as 'Losses', pDraws as 'Draws' from UserData order by pWins;"
    cursor_obj.execute(select_all_stats) 
   
    
    for head in col_heads:
        if head == 'Total Games': print("| %12s"%head, "%2s"%end, end = '')
        else: print("| %8s"%head, "%6s"%end, end = '')
    print()

    for i in cursor_obj.fetchall():
        for col in i:
            print("| %7s"%col,"%7s"%end, end = '')
       
        print()
    
    CloseCursorAndConnection(cursor_obj, connection_obj)

def SelectPlayerStats():
    cursor_obj, connection_obj = CreateCursorAndConnection()

    player = input("Enter Player Name: ")
    select_single_stats = f"select pName as 'Player', pTotal as 'Games Played', pWins as 'Wins', pLosses as 'Losses', pDraws as 'Draws' from UserData where pName = '{player}' order by pWins ;"
    cursor_obj.execute(select_single_stats) 
    
    for head in col_heads:
        if head == 'Total Games': print("| %12s"%head, "%2s"%end, end = '')
        else: print("| %8s"%head, "%6s"%end, end = '')
    print()
    
    i = cursor_obj.fetchone()
    for col in i:
        print("| %7s"%col,"%7s"%end, end = '')
    print()
    time.sleep(5)

    CloseCursorAndConnection(cursor_obj, connection_obj)

def RegisterPlayer():
    cursor_obj, connection_obj = CreateCursorAndConnection()

    while True:
        player = input("Enter Player Name: ")
        if bool(player) == False:
            print('Invalid Input. Please retry.')
            time.sleep(5)
            os.system('cls')
        else: break
    
    password = input("Enter Player Password: ")
    c_pass = input("Confirm Player Password: ")
    
    insert = f"insert into userdata(pName, pPass) values('{player}', '{password}');"
    
    if c_pass == password:
        try: 
            cursor_obj.execute(insert)
            connection_obj.commit()
            print('\nRegistration successful.')
        except: 
            connection_obj.rollback()
            print('\nError while registering. \nPlayer Name may already be registered. \nPlease retry with different Player Name.')

    CloseCursorAndConnection(cursor_obj, connection_obj)

def PlayerLogin():
    global player1, player2

    cursor_obj, connection_obj = CreateCursorAndConnection()

    while True:
        player = input("Enter Player Name: ")
        if bool(player) == False:
            print('Invalid Input. Please retry.')
            time.sleep(5)
            os.system('cls')
        elif player == player1 or player == player2:
            print('Player is already logged in. Please Retry.')
            time.sleep(5)
            os.system('cls')
        else: break

    select_pPass = f"select pPass as 'Password' from UserData where pName = '{player}';"
    cursor_obj.execute(select_pPass)
    a = cursor_obj.fetchone()
    if a and bool(a) == True: 
        password = input("Enter Player Password: ")
        
        if a[0] == password: 
            print('Login successful.')
            return player
        else: 
            print('Unsucessful login. Please retry.')
            return False            
    
    else: print('Player Name does not exist. Please Sign-In first.')
    
    CloseCursorAndConnection(cursor_obj, connection_obj)

def UpdatePlayerStats(win_player, loss_player, draw = False):
    cursor_obj, connection_obj = CreateCursorAndConnection()

    try:        
        if draw == True and win_player != loss_player:
            cursor_obj.execute(f"update userdata set pTotal = pTotal + 1, pDraws = pDraws + 1 where pName in ('{win_player}','{loss_player}');")
            print('Successfully updated data.')
        elif draw == False and win_player != loss_player:
            cursor_obj.execute(f"update userdata set pTotal = pTotal + 1, pWins = pWins + 1 where pName = '{win_player}';")
            cursor_obj.execute(f"update userdata set pTotal = pTotal + 1, pLosses = pLosses + 1 where pName = '{loss_player}';")
            print('Successfully updated data.')
        else: print('Error while updating data. Contact Admin for help.')

        connection_obj.commit()

    except: print('Error while updating data. Contact Admin for help.'); connection_obj.rollback()

    CloseCursorAndConnection(cursor_obj, connection_obj)

def Connect4_2PlayerGame():
    def new_board(board = {}):
        board = {i : [i if j==ROW_Count else '---' for j in range(ROW_Count+1)] for i in range(COL_Count)} 
        return board

    def display():
        global main_board
        for i in range(ROW_Count+1): 
            for j in range(COL_Count): 
                print('%7s'%main_board[j][-i-1], end = '\t')  
            print()
        print()

    def win_condition():
        global main_board, Human, AI, ROW_Count, COL_Count, Plot_What
        for i in range(ROW_Count-Plot_What+1):
            for j in range(COL_Count):
                col = main_board[j][i:i+Plot_What]
                if col.count(Human) == Plot_What: return f'Player 1 ({Human}) Wins!'
                elif col.count(AI) == Plot_What: return f'Player 2 ({AI}) Wins!'             

        
        for i in range(ROW_Count):
            for j in range(COL_Count-Plot_What+1):
                row = [main_board[k][i] for k in range(j, j+Plot_What)]
                if row.count(Human) == Plot_What: return f'Player 1 ({Human}) Wins!'
                elif row.count(AI) == Plot_What: return f'Player 2 ({AI}) Wins!'
                
      
        up_diag = []
        for i in range(ROW_Count-Plot_What+1):
            for j in range(COL_Count-Plot_What+1):
                up_diag = []
                for k in range(Plot_What):
                    up_diag += [main_board[j+k][i+k]]
                
                            
                if up_diag.count(Human) == Plot_What: return f'Player 1 ({Human}) Wins!'
                elif up_diag.count(AI) == Plot_What: return f'Player 2 ({AI}) Wins!'

     
        down_diag = []
        for i in range(Plot_What-1, ROW_Count):
            for j in range(COL_Count-Plot_What+1):
                down_diag = []
                for k in range(Plot_What):
                    down_diag += [main_board[j+k][i-k]]

                
                if down_diag.count(Human) == Plot_What: return f'Player 1 ({Human}) Wins!'
                elif down_diag.count(AI) == Plot_What: return f'Player 2 ({AI}) Wins!'

        count = 0
        for i in main_board:
            count += main_board[i].count('---')
        if count==0:
            return 'It is a Draw!'

        return ''
                    
    def move_maker(board, move, player):
        global ROW_Count
        for i in range(ROW_Count):
            if board[move][i]=='---':
                board[move][i] = player
                break

    def check_legal():
        global COL_Count, turn, AI, AI, main_board
        
        move = ''
        while (len(move) == 0 or move == ''):
            move = input('Enter column of choice (integer from 0 to 6): ')
        
        
        if ord(move[0])<48 or ord(move[0])>57 or len(move) == 0:
            chk_move = check_legal()
            return chk_move
        else:
            int_move = int(move)
            while int_move<0 or int_move>COL_Count-1 or main_board[int_move].count('---') == 0:       
                
                if int_move in range(7): print('Selected column is full')
                else: print('Column out of range.')
                move = check_legal()
                try:
                    int_move = int(move)
                    return int_move
                except:
                    print("Unexpected ERROR occured")
                    chk_move = check_legal()
                    return chk_move                
            
            return int_move
            
    def update(move_list, move):
        move_list += [move]        

    def undo(player, opp):
        global main_board, Human, AI, move_list, turn        
        
        a = len(move_list)
        if a <= 0:
            print('Cannot undo, board is empty.')
        else:
            del move_list[a-1:]
            a -= 1
            main_board = new_board()

            for i in range(a):
                m = move_list[i]
                if i%2==0:
                    if starter == 1:
                        move_maker(main_board, m, 'X')
                    else:
                        move_maker(main_board, m, 'O')
                else:
                    if (starter+1)%2 == 1:
                        move_maker(main_board, m, 'X')
                    else:
                        move_maker(main_board, m, 'O')
            turn = (turn+1)%2

    def all_valid_loc(board):
        global COL_Count, ROW_Count
        
        valid_loc = []
        for col in range(COL_Count):
            if board[col].count('---') != 0:
                valid_loc += [col]

        return valid_loc
    
    global main_board, turn, starter, move, move_list, ROW_Count, COL_Count, Plot_What, AI, Human
    
    turn = random.randint(0,1)
    starter = turn
    move = 0  
    move_list = []    
    main_board = new_board()
    winner = win_condition()    

    while not winner:
        menu = ' '        
        menu = input('Enter:\n"QUIT" to exit.\n"UNDO" to undo last move\nClick the "Enter" key to continue with the game: ')
        os.system('cls')
        
        if menu.upper() == 'QUIT':
            time.sleep(5)
            print("GAME OVER")
            time.sleep(5)
            return 'Game ended with QUIT'

        elif menu.upper() == 'UNDO': 
            undo(Human, AI)
            display()
            time.sleep(5)
            
        else:
            try:
                if turn == 1:
                    print(f'Player 1\'s ({Human}\'s) turn.')
                    print()
                    display()
                    move = check_legal()
                    move_maker(main_board, move, Human)
                    update(move_list, move)
                    time.sleep(5)
                    os.system('cls')
                    
                elif turn == 0 and not win_condition():                  
                    
                    print(f'Player 2\'s ({AI}\'s) turn.')
                    print()                    
                    display()
                    move = check_legal()
                    move_maker(main_board, move, AI)
                    update(move_list, move)
                    time.sleep(5)
                    os.system('cls')
              
            except: pass    
                    
            turn+=1
            turn%=2
            
            display()
            time.sleep(5)  

        if win_condition():
            print(win_condition())
            time.sleep(5)
            print("GAME OVER")
            return win_condition()
            time.sleep(5)
            break 

import random, math
turn = random.randint(0,1)
starter = turn
move = 0
move_list = []
ROW_Count = 6 
COL_Count = 7 
Plot_What = 4 
AI = 'O'
Human = 'X'
main_board = {}

import sqlite3 as SQL, time, sys, os

end = '|'
cont = 'Y'
col_heads = ('Player', 'Total Games', 'Wins', 'Losses', 'Draws')
main_over = False
sub_over = False
sub_menu = 0
main_menu = 0
player1, player2 = '', ''

main_cursor, main_connection = CreateCursorAndConnection()
if (main_cursor, main_connection) == (None, None): cont = 'no'
else: CloseCursorAndConnection(main_cursor, main_connection)

while cont.upper() == 'Y':
    main_menu = input('MAIN MENU: \n1. Single Player \n2. Two Players \n3. Leaderboard \n4. Quit \n>>> ')
   
    if main_menu in ('1', '2', '3', '4'):
        time.sleep(5)
        os.system('cls')

        if main_menu == '1':      
            import Connect4 as C4
            C4.main()
            C4.opponent_choice = ''
            C4.turn = random.randint(0,1)
            C4.starter = turn
            C4.move = 0
            C4.move_list = []
            C4.main_board = C4.new_board({}) 

        elif main_menu == '2': 
            player1, player2 = '', ''

            while sub_menu not in ('1', '2', '3', '4', '5') or sub_over == False:
                time.sleep(5)
                os.system('cls')
                sub_menu = input('2 PLAYER MODE: \n1. Sign-up \n2. Log-in  \n3. Play \n4. Log-out \n5. Show Player Stats \n6. Exit to MAIN MENU \n>>> ')
                time.sleep(5)
                os.system('cls')

                if sub_menu == '1': 
                    RegisterPlayer()
                    time.sleep(5)
                    continue

                elif sub_menu == '2':
                    if bool(player1) == False:
                        player1 = PlayerLogin()

                    elif bool(player1) == True and bool(player2) == False:
                        player2 = PlayerLogin()
                        
                    else:
                        print('Two players already logged-in. Log-out of one account to log-in.')
                    
                    time.sleep(5)
                    continue
                
                elif sub_menu == '4': 
                    log_out_player = input('Enter Player Name: ')
                    
                    if log_out_player == player1:
                        player1 = ''
                        print(f'{log_out_player} successfully Logged-Out')
                    elif log_out_player == player2: 
                        player2 = ''
                        print(f'{log_out_player} successfully Logged-Out')
                    else:
                        print('Incorrect Player Name entered, please retry.')
                    
                    time.sleep(5)
                    continue
                
                elif (player1 == '' or player2 == '') and sub_menu == '3':
                    print('This option needs 2 players to be logged in. \n\nPlease Log-In and RETRY.')
                    time.sleep(5)

                elif sub_menu == '3' and (bool(player1) == bool(player2) == True) and player1 != player2: 
                    result = Connect4_2PlayerGame()

                    if result == 'Player 1 (X) Wins!':
                        UpdatePlayerStats(win_player = player1, loss_player = player2, draw = False)
                    
                    elif result == 'Player 2 (O) Wins!':
                        UpdatePlayerStats(win_player = player2, loss_player = player1, draw = False)
                    
                    elif result == 'It is a Draw!':
                        UpdatePlayerStats(win_player = player1, loss_player = player2, draw = True)
                    
                    elif result == 'Game ended with QUIT':
                        print('Someone QUIT the game!')                        
                    
                    else:
                        print('ERROR! The game ended unexpectedly.')

                    time.sleep(5)
                    result = ''

                elif sub_menu == '5':
                    SelectPlayerStats()
                    continue
                
                elif sub_menu == '6':
                    sub_over = True
                    break

                else:
                    print('Invalid input. Please RETRY.')

        elif main_menu == '3':
            SelectAllPlayerStats()
            
        elif main_menu == '4':
            time.sleep(5)
            sys.exit("GAME OVER")
            time.sleep(5)

    if main_menu in ('1', '2', '3', '4'):
        cont = input('\nPress "Y" to continue. Press any other key to exit. ')
    else: 
        cont = input('\nERROR in input. \nPress "Y" to retry. \nPress any other key to exit. \n> ')
    
    time.sleep(5)
    os.system('cls')

#==============================================================================================================================================================================================================================================================================

