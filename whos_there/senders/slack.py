from typing import List, Any, Optional

from whos_there.senders.base import Sender


class SlackSender(Sender):
    def __init__(self, webhook_url: str, channel: str, user_mentions: List[str] = []) -> None:
        """Initialize the Slack sender.

        Args:
            webhook_url: The Slack webhook URL.
            channel: The Slack channel name.
            user_mentions: The list of users to mention.
        """
        super().__init__()
        self.webhook_url = webhook_url
        self.channel = channel
        self.user_mentions = " ".join(user_mentions)

    def send(self, payload: Any) -> None:    
        data = {
            "username": "Knock Knock",
            "channel": self.channel,
            "link_names": 1,
            "icon_emoji": ":clapper:",  # ":tada:"
        }
        if isinstance(payload, tuple) or isinstance(payload, list):
            data.update({"blocks": self._get_text_block(text) + blocks})
        else:
            data.update({"text": f"{text} {self.user_mentions}")
        
        return self._send_json(self.webhook_url, data)

    def _get_text_block(self, text):
      return [{"type": "section",
               "text": {
                  "type": "mrkdwn",
                  "text": f"{text} {self.user_mentions}",
              }}]
