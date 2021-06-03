#Program to scrape and clean game data from basketball-reference.com

import csv
import pandas as pd


class Preprocessing:

    def __init__(self):

        months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
        years = ['2015', '2016', '2017', '2018', '2019']
        str = 'https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html'
        url_list = []
        for year in years:
            for month in months:
                url_list.append(str.format(year, month))

        visitor_teams = []
        visitor_points = []
        home_teams = []
        home_points = []

        for url in url_list:
            df = pd.read_html(url, header = 0)
            for (column, col_data) in df[0].iteritems():
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

        # print(len(visitor_teams), len(visitor_points), len(home_points), len(home_teams))

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
        df_obj.to_csv("total_results.csv")

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
        self.final_dataframe.to_csv("final_dataframe.csv")


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
