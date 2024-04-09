import os
import logging
from datetime import datetime, timedelta
from telegram import Update, ChatMemberStatus
from telegram.ext import Updater, CommandHandler, CallbackContext

# 设置你的机器人token
TOKEN = os.environ.get('TELEGRAM_TOKEN')

# 设置管理员列表
ADMINS = [1234567890]  # 将数字替换为你的Telegram用户ID

# 设置日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 记录每天在群里发言的成员user_id
daily_active_users = set()

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('欢迎使用群组管理机器人!')

def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('我踏马来啦~')

def purge_inactive(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in ADMINS:
        update.message.reply_text('你没有权限执行此操作。')
        return

    chat_id = update.message.chat_id
    
    # 获取群组成员列表
    members = context.bot.get_chat_members_count(chat_id)
    
    # 获取30天前的时间
    last_month = datetime.now() - timedelta(days=30)
    
    # 遍历成员列表,移除不活跃的成员
    purged = 0
    for member in members:
        if member.status == ChatMemberStatus.KICKED:
            # 已删除账号
            purged += 1
        elif member.user.id not in daily_active_users:  
            # 30天内没发言
            try:
                context.bot.ban_chat_member(chat_id, member.user.id)
                purged += 1
            except Exception as e:
                logger.warning(f'移除成员 {member.user.id} 失败: {str(e)}')
        elif member.user.status.was_online < last_month:
            # 30天没上线
            try:
                context.bot.ban_chat_member(chat_id, member.user.id)
                purged += 1  
            except Exception as e:
                logger.warning(f'移除成员 {member.user.id} 失败: {str(e)}')
    
    update.message.reply_text(f'已移除 {purged} 名不活跃成员。')

def log_daily_active(context: CallbackContext) -> None:
    # 每天记录当天发言的成员
    global daily_active_users
    daily_active_users = set()
    
    # 获取所有群组
    chats = context.bot.get_updates()
    for chat in chats:
        try:
            # 获取当天发言的成员
            members = context.bot.get_chat_members_count(chat.message.chat_id)
            for member in members:
                daily_active_users.add(member.user.id)
        except Exception as e:
            logger.warning(f'获取群组 {chat.message.chat_id} 成员失败: {str(e)}')

def main() -> None:
    PORT = int(os.environ.get('PORT', '8443'))
    APP_URL = os.environ.get('APP_URL')

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ping", ping))
    dispatcher.add_handler(CommandHandler("purge", purge_inactive))
    
    # 设置每天执行一次的job
    updater.job_queue.run_daily(log_daily_active, time=datetime.time(0, 0, 0))

    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN,
                          webhook_url=APP_URL + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
