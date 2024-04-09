# Telegram 群组管理机器人

这是一个用于管理 Telegram 群组的机器人,主要功能包括:

- 自动踢出删除帐号的成员
- 自动踢出30天内没有在群组发言的成员
- 自动踢出30天内没有登录 Telegram 的成员
- 支持 /ping 命令检查机器人在线状态
- 支持 /purge 命令手动清理不活跃成员(需要管理员权限)


部署前需要准备:

- 一个 Telegram 机器人的 Token,可以通过 [@BotFather](https://t.me/BotFather) 申请
- 你自己的 Telegram 用户 ID,将用于识别管理员身份,可以通过 [@userinfobot](https://t.me/userinfobot) 获取
- 一个 Heroku 帐号,如果没有可以 [免费注册](https://signup.heroku.com/)

部署步骤:

1. 点击上面的 "Deploy to Heroku" 按钮
2. 在 Heroku 的 deployment 页面填写 App 名称、地区,然后点击 "Deploy app" 按钮
3. 等待部署完成,如果成功页面底部会显示 "Your app was successfully deployed" 
4. 点击 "Manage App" 进入应用管理页面,在 Settings -> Config Vars 中添加配置变量:
   - TELEGRAM_TOKEN : 你的机器人 Token
   - ADMIN_ID : 你的用户 ID
5. 在 Resources 页面将 worker 的 Dyno 设为启用
6. 至此部署完成,你可以在 Telegram 中与机器人对话测试功能

## 使用

- 将机器人添加到群组,并给予管理员权限
- 使用 /ping 命令检查机器人是否在线
- 使用 /purge 命令手动清理不活跃成员(需要管理员权限)
- 机器人会自动清理不活跃成员,默认为每天 0 点进行清理

## 注意事项

- Heroku 的免费 dyno 每个月有 550 小时的额度,超过部分需要付费
- Heroku 的免费 dyno 30 分钟内没有请求会自动休眠,可以使用第三方监控服务定时 ping
- 本项目仅供学习交流使用,请遵守 Telegram 的机器人使用规范,不要滥用

## 参考资料

- [python-telegram-bot 文档](https://python-telegram-bot.readthedocs.io/)
- [Heroku 官方文档](https://devcenter.heroku.com/)
- [用 Python 开发 Telegram Bot](https://blog.csdn.net/qq_41185868/article/details/80570200)

## License

[MIT License](LICENSE)


