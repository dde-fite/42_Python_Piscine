from random import shuffle
from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: list[TournamentCard] = []

    def get_card(self, card_id: str) -> TournamentCard | None:
        for card in self.cards:
            if card.id == card_id:
                return card
        return None

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        stats = card.get_tournament_stats()
        return (f"{card.get_card_info()['name']} (ID: {card.id})\n"
                f"- Interfaces [Card, Combatable, Rankable]\n"
                f"- Rating: {card.calculate_rating()}\n"
                f"- Record: {stats['wins']}-{stats['losses']}")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if (not (card_1 := self.get_card(card1_id))
           or not (card_2 := self.get_card(card2_id))):
            return {'error': 'Incorrect card IDs'}
        participants: list[TournamentCard] = [card_1, card_2]
        shuffle(participants)
        winner = participants[0]
        loser = participants[1]
        winner.update_wins(1)
        loser.update_losses(1)
        return {
            'winner': winner.id,
            'loser': loser.id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
