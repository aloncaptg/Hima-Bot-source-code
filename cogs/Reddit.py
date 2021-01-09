from discord.ext import commands
from discord import Embed, Color
import aiohttp
import random
import asyncio


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.colors = (Color.red(), Color.gold(), Color.green(),
                       Color.magenta(), Color.teal(), Color.dark_blue())
        self.bot = bot
        self.session = aiohttp.ClientSession(
            headers={'User-agent': 'RedditCrawler'})

    @commands.command(name="subran", aliases=['subredditrandom', 'subredrandom'])
    @commands.cooldown(1, 5, type=commands.BucketType.user)
    async def subreddit_random(self, ctx, subreddit_name: str):
        """Gets a random post from the provided sub-reddit and posts it"""
        await ctx.trigger_typing()
        data = await self.get_res_data(f"r/{subreddit_name}/random", {'limit': 1})
        await self.send_post(ctx, data[0]['data']['children'][0])

    @commands.command(name="meme", aliases=['memez', 'memes'])
    @commands.cooldown(1, 5, type=commands.BucketType.user)
    async def meme(self, ctx):
        """Gets a random meme from the r/memes sub-reddit and posts it"""
        await ctx.trigger_typing()
        data = await self.get_res_data(f"r/memes/random", {'limit': 1})
        await self.send_post(ctx, data[0]['data']['children'][0])

    async def random_from_post_list(self, ctx, url_part: str, params: dict):
        await ctx.trigger_typing()
        res = await self.get_res_data(url_part, params)

        # Send the error and return
        error = res.get('error')
        if error:
            await ctx.send(f"What if you wanted to see a post, but Reddit said:\n{error} {res.get('message')}")
            return

        # Get the raw list of posts
        posts = res['data']['children']

        # Filter the posts
        posts = list(filter(self.post_safe_filter, posts))

        # If no posts went through the filter, then reply and return
        if not posts:
            await ctx.send("Couldn't find any posts :(")
            return

        # Grab a random post
        post = random.choice(posts)

        await self.send_post(ctx, post)

    async def get_res_data(self, url_part, params):
        async with self.session.get(f"https://reddit.com/{url_part}.json", params=params) as response:
            return await response.json()

    async def send_post(self, ctx, post):
        post = post['data']

        # Extract info to be used
        img_url = post.get('url')
        title = post.get('title')
        ups = post.get('ups')
        num_comments = post.get('num_comments')

        embed = Embed(title=title, description = f'Credits : {img_url}',color=random.choice(self.colors))
        embed.set_image(url=img_url)
        # TODO: Use unicode instead of emojis directly
        embed.set_footer(text=f"👍 {ups} | 💬 {num_comments}")
        await ctx.send(embed=embed)

    def post_safe_filter(self, post):
        return(
            post['data']['is_reddit_media_domain'] and
            not post['data']['over_18']
        )

    async def close_session(self):
        await self.session.close()


def setup(bot):
    bot.add_cog(Reddit(bot))


def teardown(bot: commands.Bot):
    reddit_cog = bot.get_cog('Reddit')
    asyncio.run(reddit_cog.close_session())