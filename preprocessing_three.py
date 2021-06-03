#Program to scrape and clean game data from basketball-reference.com

import csv
import pandas as pd


class PreprocessingThree:

    def __init__(self):

        #https://www.basketball-reference.com/boxscores/201410280NOP.html
        #https://www.basketball-reference.com/boxscores/201501010CHI.html

        months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
        years = ['2015', '2016', '2017', '2018', '2019']
        web = 'https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html'
        url_list = []
        for year in years:
            for month in months:
                url_list.append(web.format(year, month))

        visitor_teams = []
        visitor_points = []
        home_teams = []
        home_points = []
        game_date = []

        for url in url_list:
            df = pd.read_html(url, header = 0)
            for (column, col_data) in df[0].iteritems():
                if column == 'Date':
                    for data in col_data.values:
                        if data == 'Playoffs':
                            break
                        game_date.append(data)
                if column == 'Visitor/Neutral':
                    for data in col_data.values:
                        if data == 'Playoffs':
                            break
                        visitor_teams.append(data)
                if column == 'PTS':
                    for data in col_data.values:
                        if data == 'Playoffs':
                            break
                        visitor_points.append(data)
                if column == 'Home/Neutral':
                    for data in col_data.values:
                        if data == 'Playoffs':
                            break
                        home_teams.append(data)
                if column == 'PTS.1':
                    for data in col_data.values:
                        if data == 'Playoffs':
                            break
                        home_points.append(data)

        code = ''
        code_list = []

        for date in game_date:
            if len(date) == 17:
                if date[9] != ' ':
                    if 'Oct' in date:
                        code = date[13:17] + '10' + date[9:11] + '0'
                    if 'Nov' in date:
                        code = date[13:17] + '11' + date[9:11] + '0'
                    if 'Dec' in date:
                        code = date[13:17] + '12' + date[9:11] + '0'
                    if 'Jan' in date:
                        code = date[13:17] + '01' + date[9:11] + '0'
                    if 'Feb' in date:
                        code = date[13:17] + '02' + date[9:11] + '0'
                    if 'Mar' in date:
                        code = date[13:17] + '03' + date[9:11] + '0'
                    if 'Apr' in date:
                        code = date[13:17] + '04' + date[9:11] + '0'
                else:
                    if 'Oct' in date:
                        code = date[13:17] + '10' + '0' + date[10:11] + '0'
                    if 'Nov' in date:
                        code = date[13:17] + '11' + '0' + date[10:11] + '0'
                    if 'Dec' in date:
                        code = date[13:17] + '12' + '0' + date[10:11] + '0'
                    if 'Jan' in date:
                        code = date[13:17] + '01' + '0' + date[10:11] + '0'
                    if 'Feb' in date:
                        code = date[13:17] + '02' + '0' + date[10:11] + '0'
                    if 'Mar' in date:
                        code = date[13:17] + '03' + '0' + date[10:11] + '0'
                    if 'Apr' in date:
                        code = date[13:17] + '04' + '0' + date[10:11] + '0'
                code_list.append(code)
            else:
                code = date[12:16]
                if date[8] != ' ':
                    if 'Oct' in date:
                        code = date[12:16] + '10' + date[8:10] + '0'
                    if 'Nov' in date:
                        code = date[12:16] + '11' + date[8:10] + '0'
                    if 'Dec' in date:
                        code = date[12:16] + '12' + date[8:10] + '0'
                    if 'Jan' in date:
                        code = date[12:16] + '01' + date[8:10] + '0'
                    if 'Feb' in date:
                        code = date[12:16] + '02' + date[8:10] + '0'
                    if 'Mar' in date:
                        code = date[12:16] + '03' + date[8:10] + '0'
                    if 'Apr' in date:
                        code = date[12:16] + '04' + date[8:10] + '0'
                else:
                    if 'Oct' in date:
                        code = date[12:16] + '10' + '0' + date[9:10] + '0'
                    if 'Nov' in date:
                        code = date[12:16] + '11' + '0' + date[9:10] + '0'
                    if 'Dec' in date:
                        code = date[12:16] + '12' + '0' + date[9:10] + '0'
                    if 'Jan' in date:
                        code = date[12:16] + '01' + '0' + date[9:10] + '0'
                    if 'Feb' in date:
                        code = date[12:16] + '02' + '0' + date[9:10] + '0'
                    if 'Mar' in date:
                        code = date[12:16] + '03' + '0' + date[9:10] + '0'
                    if 'Apr' in date:
                        code = date[12:16] + '04' + '0' + date[9:10] + '0'
                code_list.append(code)

        for i in range(len(home_teams)):
            if home_teams[i] == 'New Orleans Pelicans':
                code_list[i] = code_list[i] + 'NOP'
            if home_teams[i] == 'San Antonio Spurs':
                code_list[i] = code_list[i] + 'SAS'
            if home_teams[i] == 'Los Angeles Lakers':
                code_list[i] = code_list[i] + 'LAL'
            if home_teams[i] == 'Charlotte Hornets':
                code_list[i] = code_list[i] + 'CHO'
            if home_teams[i] == 'Indiana Pacers':
                code_list[i] = code_list[i] + 'IND'
            if home_teams[i] == 'Toronto Raptors':
                code_list[i] = code_list[i] + 'TOR'
            if home_teams[i] == 'Miami Heat':
                code_list[i] = code_list[i] + 'MIA'
            if home_teams[i] == 'Boston Celtics':
                code_list[i] = code_list[i] + 'BOS'
            if home_teams[i] == 'New York Knicks':
                code_list[i] = code_list[i] + 'NYK'
            if home_teams[i] == 'Memphis Grizzlies':
                code_list[i] = code_list[i] + 'MEM'
            if home_teams[i] == 'Denver Nuggets':
                code_list[i] = code_list[i] + 'DEN'
            if home_teams[i] == 'Utah Jazz':
                code_list[i] = code_list[i] + 'UTA'
            if home_teams[i] == 'Phoenix Suns':
                code_list[i] = code_list[i] + 'PHO'
            if home_teams[i] == 'Sacramento Kings':
                code_list[i] = code_list[i] + 'SAC'
            if home_teams[i] == 'Portland Trail Blazers':
                code_list[i] = code_list[i] + 'POR'
            if home_teams[i] == 'Orlando Magic':
                code_list[i] = code_list[i] + 'ORL'
            if home_teams[i] == 'Cleveland Cavaliers':
                code_list[i] = code_list[i] + 'CLE'
            if home_teams[i] == 'Minnesota Timberwolves':
                code_list[i] = code_list[i] + 'MIN'
            if home_teams[i] == 'Dallas Mavericks':
                code_list[i] = code_list[i] + 'DAL'
            if home_teams[i] == 'Los Angeles Clippers':
                code_list[i] = code_list[i] + 'LAC'
            if home_teams[i] == 'Chicago Bulls':
                code_list[i] = code_list[i] + 'CHI'
            if home_teams[i] == 'Milwaukee Bucks':
                code_list[i] = code_list[i] + 'MIL'
            if home_teams[i] == 'Philadelphia 76ers':
                code_list[i] = code_list[i] + 'PHI'
            if home_teams[i] == 'Washington Wizards':
                code_list[i] = code_list[i] + 'WAS'
            if home_teams[i] == 'Atlanta Hawks':
                code_list[i] = code_list[i] + 'ATL'
            if home_teams[i] == 'Detroit Pistons':
                code_list[i] = code_list[i] + 'DET'
            if home_teams[i] == 'Houston Rockets':
                code_list[i] = code_list[i] + 'HOU'
            if home_teams[i] == 'Oklahoma City Thunder':
                code_list[i] = code_list[i] + 'OKC'
            if home_teams[i] == 'Golden State Warriors':
                code_list[i] = code_list[i] + 'GSW'
            if home_teams[i] == 'Brooklyn Nets':
                code_list[i] = code_list[i] + 'BRK'

        web = 'https://www.basketball-reference.com/boxscores/{}.html'
        url_list = []
        for code in code_list:
            url_list.append(web.format(code))

        for url in url_list:
            df = pd.read_html(url, header = 0)
            print(df)
            break

        # print(df)


        for i in range(len(visitor_points)):
            visitor_points[i] = int(visitor_points[i])
            home_points[i] = int(home_points[i])

        winner = []
        for i in range(len(visitor_points)):
            if visitor_points[i] > home_points[i]:
                winner.append(visitor_teams[i])
            elif visitor_points[i] < home_points[i]:
                winner.append(home_teams[i])

        merged_list = [(visitor_teams[i], visitor_points[i], home_teams[i], home_points[i], winner[i]) for i in range(0, len(visitor_points))]
        df_obj = pd.DataFrame(merged_list, columns=['away', 'vis_pts', 'home', 'home_pts', "winner"])
        # print(df_obj)
        df_obj.to_csv("total_results_three.csv")

        all_teams = []
        wins_per_team = {}
        losses_per_team = {}
        win_loss_percentage = {}
        wins_per_team_at_home = {}
        losses_per_team_at_home = {}
        wins_per_team_at_away = {}
        losses_per_team_at_away = {}
        vis_win_loss_percentage = {}
        home_win_loss_percentage = {}
        point_diff_pg = {}
        prev_eight_games_log = {}
        prev_eight_games_wins = {}
        prev_eight_games_losses = {}
        prev_eight_games_percentage = {}
        new_dataframe = {}
        store_data_per_team = {}

        for team in home_teams:
            if team not in all_teams:
                all_teams.append(team)
                wins_per_team[team] = 0
                losses_per_team[team] = 0
                win_loss_percentage[team] = 0
                wins_per_team_at_home[team] = 0
                losses_per_team_at_home[team] = 0
                wins_per_team_at_away[team] = 0
                losses_per_team_at_away[team] = 0
                vis_win_loss_percentage[team] = 0
                home_win_loss_percentage[team] = 0
                point_diff_pg[team] = 0
                prev_eight_games_log[team] = []
                prev_eight_games_wins[team] = 0
                prev_eight_games_losses[team] = 0
                prev_eight_games_percentage[team] = 0
                store_data_per_team[team] = (0,0,0,0)
            if len(all_teams) == 30:
                break

        new_dataframe = {}

        for ind in df_obj.index:
            # if ind == 3690:
            #     break

            if ind == 1230 or ind == 2460 or ind == 3690 or ind == 4920:
                for team in all_teams:
                    wins_per_team[team] = 0
                    losses_per_team[team] = 0
                    win_loss_percentage[team] = 0
                    wins_per_team_at_home[team] = 0
                    losses_per_team_at_home[team] = 0
                    wins_per_team_at_away[team] = 0
                    losses_per_team_at_away[team] = 0
                    vis_win_loss_percentage[team] = 0
                    home_win_loss_percentage[team] = 0
                    point_diff_pg[team] = 0
                    prev_eight_games_log[team] = []
                    prev_eight_games_wins[team] = 0
                    prev_eight_games_losses[team] = 0
                    prev_eight_games_percentage[team] = 0
                    store_data_per_team[team] = (0,0,0,0)

            if df_obj['home'][ind] == df_obj['winner'][ind]:
                new_dataframe[ind] = store_data_per_team[df_obj['home'][ind]] + store_data_per_team[df_obj['away'][ind]] + (1,)
            else:
                new_dataframe[ind] = store_data_per_team[df_obj['home'][ind]] + store_data_per_team[df_obj['away'][ind]] + (0,)


            #calculate win/loss percentage for home and away teams up to that point in time
            #calculate home win/loss percentage for home teams up to that point in time
            #calculate away win/loss percentage for away teams up to that point in time
            #calculate point difference per team up to that point in time
            #calculate win/loss percentage for last eight games played up to that point in time
            if df_obj['home'][ind] == df_obj['winner'][ind]:
                wins_per_team[df_obj['home'][ind]] += 1
                losses_per_team[df_obj['away'][ind]] += 1
                wins_per_team_at_home[df_obj['home'][ind]] += 1
                losses_per_team_at_away[df_obj['away'][ind]] += 1
            else:
                losses_per_team[df_obj['home'][ind]] += 1
                wins_per_team[df_obj['away'][ind]] += 1
                losses_per_team_at_home[df_obj['home'][ind]] += 1
                wins_per_team_at_away[df_obj['away'][ind]] += 1
            win_loss_percentage[df_obj['home'][ind]] = wins_per_team[df_obj['home'][ind]] / (wins_per_team[df_obj['home'][ind]]
                                                                                + losses_per_team[df_obj['home'][ind]])
            win_loss_percentage[df_obj['away'][ind]] = wins_per_team[df_obj['away'][ind]] / (wins_per_team[df_obj['away'][ind]]
                                                                                + losses_per_team[df_obj['away'][ind]])
            point_diff_pg[df_obj['home'][ind]] += df_obj['home_pts'][ind] - df_obj['vis_pts'][ind]
            point_diff_pg[df_obj['away'][ind]] += df_obj['vis_pts'][ind] - df_obj['home_pts'][ind]

            home_win_loss_percentage[df_obj['home'][ind]] = wins_per_team_at_home[df_obj['home'][ind]] / (wins_per_team_at_home[df_obj['home'][ind]]
                                                                                            + losses_per_team_at_home[df_obj['home'][ind]])
            vis_win_loss_percentage[df_obj['away'][ind]] = wins_per_team_at_away[df_obj['away'][ind]] / (wins_per_team_at_away[df_obj['away'][ind]]
                                                                                            + losses_per_team_at_away[df_obj['away'][ind]])
            if len(prev_eight_games_log[df_obj['home'][ind]]) < 8:
                if [df_obj['home'][ind]] == [df_obj['winner'][ind]]:
                    prev_eight_games_log[df_obj['home'][ind]].append('W')
                else:
                    prev_eight_games_log[df_obj['home'][ind]].append('L')
            else:
                prev_eight_games_log[df_obj['home'][ind]].pop(0)
                if [df_obj['home'][ind]] == [df_obj['winner'][ind]]:
                    prev_eight_games_log[df_obj['home'][ind]].append('W')
                else:
                    prev_eight_games_log[df_obj['home'][ind]].append('L')
            if len(prev_eight_games_log[df_obj['away'][ind]]) < 8:
                if [df_obj['away'][ind]] == [df_obj['winner'][ind]]:
                    prev_eight_games_log[df_obj['away'][ind]].append('W')
                else:
                    prev_eight_games_log[df_obj['away'][ind]].append('L')
            else:
                prev_eight_games_log[df_obj['away'][ind]].pop(0)
                if [df_obj['away'][ind]] == [df_obj['winner'][ind]]:
                    prev_eight_games_log[df_obj['away'][ind]].append('W')
                else:
                    prev_eight_games_log[df_obj['away'][ind]].append('L')

            prev_eight_games_wins[df_obj['home'][ind]] = 0
            prev_eight_games_losses[df_obj['home'][ind]] = 0
            prev_eight_games_wins[df_obj['away'][ind]] = 0
            prev_eight_games_losses[df_obj['away'][ind]] = 0
            for outcome in prev_eight_games_log[df_obj['home'][ind]]:
                if outcome == 'W':
                    prev_eight_games_wins[df_obj['home'][ind]] +=1
                else:
                    prev_eight_games_losses[df_obj['home'][ind]] +=1
            for outcome in prev_eight_games_log[df_obj['away'][ind]]:
                if outcome == 'W':
                    prev_eight_games_wins[df_obj['away'][ind]] +=1
                else:
                    prev_eight_games_losses[df_obj['away'][ind]] +=1
            prev_eight_games_percentage[df_obj['home'][ind]] = prev_eight_games_wins[df_obj['home'][ind]] / (prev_eight_games_wins[df_obj['home'][ind]] + prev_eight_games_losses[df_obj['home'][ind]])
            prev_eight_games_percentage[df_obj['away'][ind]] = prev_eight_games_wins[df_obj['away'][ind]] / (prev_eight_games_wins[df_obj['away'][ind]] + prev_eight_games_losses[df_obj['away'][ind]])
            store_data_per_team[df_obj['home'][ind]] = (win_loss_percentage[df_obj['home'][ind]], point_diff_pg[df_obj['home'][ind]],
                                        home_win_loss_percentage[df_obj['home'][ind]], prev_eight_games_percentage[df_obj['home'][ind]])
            store_data_per_team[df_obj['away'][ind]] = (win_loss_percentage[df_obj['away'][ind]], point_diff_pg[df_obj['away'][ind]],
                                        vis_win_loss_percentage[df_obj['away'][ind]], prev_eight_games_percentage[df_obj['away'][ind]])

        final_datalist = []

        for row in new_dataframe:
            final_datalist.append(new_dataframe[row])

        self.final_dataframe = pd.DataFrame(final_datalist, columns=['home_win_loss_percentage', 'home_point_diff_total', 'home_win_loss_at_home_percentage',
                        'home_prev_eight_game_percentage', 'away_win_loss_percentage', 'away_point_diff_total', 'away_win_loss_at_away_percentage',
                                        'away_prev_eight_game_percentage', 'winner'])

        # print(self.final_dataframe)
        self.final_dataframe.to_csv("final_dataframe_three.csv")


        ###Code used to check that my data cleaning process was succesful
        sort_winners = sorted(wins_per_team.items(), key=lambda x: x[1], reverse=True)
        sort_losers = sorted(losses_per_team.items(), key=lambda x: x[1])
        sort_per = sorted(win_loss_percentage.items(), key=lambda x: x[1], reverse=True)
        sort_winners_at_home = sorted(wins_per_team_at_home.items(), key=lambda x: x[1], reverse=True)
        sort_losers_at_home = sorted(losses_per_team_at_home.items(), key=lambda x: x[1])
        sort_winners_at_away = sorted(wins_per_team_at_away.items(), key=lambda x: x[1], reverse=True)
        sort_losers_at_away = sorted(losses_per_team_at_away.items(), key=lambda x: x[1])
        sort_per_at_home = sorted(home_win_loss_percentage.items(), key=lambda x: x[1], reverse=True)
        sort_per_at_away = sorted(vis_win_loss_percentage.items(), key=lambda x: x[1], reverse=True)
        sort_pdpg = sorted(point_diff_pg.items(), key=lambda x: x[1], reverse=True)
        sort_prev_eight_winners = sorted(prev_eight_games_wins.items(), key=lambda x: x[1], reverse=True)
        sort_prev_eight_losers = sorted(prev_eight_games_losses.items(), key=lambda x: x[1])
        sort_prev_eight_percentage = sorted(prev_eight_games_percentage.items(), key=lambda x: x[1], reverse=True)
        #
        #
        # for i in range(len(sort_winners)):
        #       # print(sort_winners[i], sort_losers[i], sort_per[i], sort_pdpg[i])
        #       # print(sort_winners_at_home[i], sort_losers_at_home[i], sort_winners_at_away[i], sort_losers_at_away[i])
        #       print(sort_prev_eight_winners[i], sort_prev_eight_losers[i], sort_prev_eight_percentage[i])
