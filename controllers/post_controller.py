from models.post import Post
from models.marp import Marp

class PostController:
    def create_post(self, uuid: str, marp: Marp):
        post = Post(uuid=uuid, content=marp.content, style=marp.style)
        post.save()
        return {"message": "Post created successfully"}

    def get_post(self, uuid: str):
        post = Post.get_by_uuid(uuid)
        if post:
            return {"content": post.content, "style": post.style}
        else:
            raise HTTPException(status_code=404, detail="Post not found")
