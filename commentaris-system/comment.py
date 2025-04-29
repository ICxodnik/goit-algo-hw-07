import uuid
from typing import Union, List

class Comment:

    def __init__(self, text: str, author: str):
        self.id = str(uuid.uuid4())
        self.text:str = text
        self.author:str = author
        self.replies: List[Comment] = []
        self.is_deleted:bool = False

    def __str__(self):
        if self.author is None:
            return self.text
        return f"{self.author}: {self.text}"
    
    def __repr__(self):
        return f"Comment(id={self.id}, author={self.author}, is_deleted={self.is_deleted})"

    def display(self, level=0):
        indent = "    " * level
        print(indent + str(self))
        for reply in self.replies:
            reply.display(level + 1)

    def add_reply(self, reply: 'Comment'):
        if not isinstance(reply, Comment):
            raise TypeError("Reply must be an instance of Comment")
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено." 
        self.author = None
        self.is_deleted = True

    def remove_reply_by_id(self, comment_id: str):
        for reply in self.replies:
            if reply.id == comment_id:
                reply.remove_reply()
                break

    def find_by_id(self, comment_id: str) -> Union['Comment', None]:
        if self.id == comment_id:
            return self
        for reply in self.replies:
            found = reply.find_by_id(comment_id)
            if found:
                return found
        return None
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "author": self.author,
            "is_deleted": self.is_deleted,
            "replies": [reply.to_dict() for reply in self.replies]
        }

if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
