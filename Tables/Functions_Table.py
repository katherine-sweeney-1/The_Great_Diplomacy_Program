from Class_Table import Table

def yield_table (commands, game_and_turn):
    db_table = Table()
    db_table.create_table(game_and_turn)
    db_table.delete_previous_data(game_and_turn)
    db_table.save(commands, game_and_turn)
    return db_table