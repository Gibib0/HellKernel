import json
from pathlib import Path
from turtledemo.clock import current_day


class StateManager:
    def __init__(self):
        self.current_act = 1
        self.keys_found = [False, False, False, False, False]
        self.corruption_level = 0.0
        self._setup_paths()

    def _setup_paths(self):
        PROJECT_ROOT = Path(__file__).parent.parent.parent

        self.SAVES_DIR = PROJECT_ROOT / 'saves'
        self.SAVES_DIR.mkdir(exist_ok=True)

        self.SAVE_FILE_PATH = self.SAVES_DIR / 'game_save.json'

        self.ASSETS_DIR = PROJECT_ROOT / 'assets'

    def unlock_key(self, key_index):
        if 0 <= key_index < len(self.keys_found):
            self.keys_found[key_index] = True
            print(f'The key {key_index + 1} is found')

            self._check_act_transitions()

            self.save_game()
        else:
            print(f'Error: wrong index of key {key_index}')

    def _check_act_transitions(self):
        previous_act = self.current_act

        if self.current_act == 1 and self.keys_found[0]:
            self.current_act = 2
        elif self.current_act == 2 and self.keys_found[2]:
            self.current_act = 3
        elif self.current_act == 3 and self.keys_found[3]:
            self.current_act = 4

        if previous_act != self.current_act:
            print(f'Transition to act {self.current_act}')

    def get_found_keys_count(self):
        return sum(self.keys_found)

    def is_all_keys_found(self):
        return all(self.keys_found)

    def save_game(self):
        save_data = {
            'current_act': self.current_act,
            'keys_found': self.keys_found,
            'corruption_level': self.corruption_level
        }

        try:
            with open(self.SAVE_FILE_PATH, 'w', encoding='utf-8') as file:
                json.dump(save_data, file, indent=4, ensure_ascii=False)
            print('The game is saved')
        except Exception as e:
            print(f'Save error {e}')

    def load_game(self):
        if not self.SAVE_FILE_PATH.exists():
            print('The save file is not found. Start new game')
            return False

        try:
            with open(self.SAVE_FILE_PATH, 'r', encoding='utf-8') as file:
                save_data = json.load(file)

                self.current_act = save_data.get('current_act', 1)
                self.keys_found = save_data.get('keys_found', [False, False, False, False, False])
                self.corruption_level = save_data.get('corruption_level', 0.0)

                print('The game is loaded')
                return True
        except Exception as e:
            print(f'Load error {e}')
            return False

    def reset_game(self):
        self.current_act = 1
        self.keys_found = [False, False, False, False, False]
        self.corruption_level = 0.0
        print('The game reset')

        if self.SAVE_FILE_PATH.exists():
            self.SAVE_FILE_PATH.unlink()

if __name__ == '__main__':
    print('Testing StateManager...')

    state = StateManager()

    print(f'The initial act: {state.current_act}')
    print(f'Keys found: {state.get_found_keys_count()}')

    state.unlock_key(0)
    print(f'Act after the first key: {state.current_act}')

    state.unlock_key(2)
    print(f'Act after the third key: {state.current_act}')

    state.save_game()

    state2 = StateManager()
    state2.load_game()
    print(f'The loaded act: {state2.current_act}')