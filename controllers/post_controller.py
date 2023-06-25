from models.post import Post
from models.marp import Marp
from datetime import datetime
import pytz

class PostController:
    def create_post(self, uuid: str, marp: Marp):
        Post.delete_by_uuid(uuid)
        post = Post(uuid=uuid, content=marp.content, style=marp.style)
        post.save()
        return {"message": "Post created successfully"}

    def get_post(self, uuid: str):
        post = Post.get_by_uuid(uuid)
        now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")

        if post and (datetime.strptime(now, "%Y-%m-%d %H:%M:%S") - datetime.strptime(post.created_at, "%Y-%m-%d %H:%M:%S")).total_seconds() < 60 * 30:
            return {"content": post.content, "style": post.style, "created_at": post.created_at}
        elif post:
            return {"message": "Post expired"}
        else:
            raise HTTPException(status_code=404, detail="Post not found")

    def get_posts(self):
        posts = Post.get_all()
        return posts