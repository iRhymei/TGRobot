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

Citations:
[1] https://blog.51cto.com/u_6740008/4852594
[2] https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh/blob/master/docs/%E7%AC%AC%E5%8D%81%E5%85%AB%E7%AB%A0%EF%BC%9AHeroku%E4%B8%8A%E7%9A%84%E9%83%A8%E7%BD%B2.md
[3] https://lpd-ios.github.io/2017/07/11/GitHub-Wiki-Introduction/
[4] http://xiaocong.github.io/blog/2013/03/20/team-collaboration-with-github/
[5] https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
[6] https://www.jianshu.com/p/9ab92efc286a
[7] https://github.com/liangshimeng/heroku-v2ray2.0
[8] https://yuuichung.github.io/2018/06/06/hexo-readme/
[9] https://github.com/guodongxiaren/README
[10] https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
[11] https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github
[12] https://blog.csdn.net/weixin_38419133/article/details/88877175
[13] https://www.volcengine.com/theme/3800988-R-7-1
[14] https://github.com/anuraghazra/github-readme-stats/blob/master/docs/readme_cn.md
[15] https://github.com/peng-zhihui/Dummy-Robot/blob/main/README.md
[16] https://github.com/Hubery-Lee/Notes/blob/master/%E5%A6%82%E4%BD%95%E5%9C%A8github%E4%B8%8A%E5%86%99%E5%87%BA%E6%BC%82%E4%BA%AE%E7%9A%84readme.md.md
[17] https://github.com/zhayujie/bot-on-anything/blob/master/README.md
[18] https://github.com/kaivin/markdown/blob/master/readme.md
[19] https://github.com/qhduan/ConversationalRobotDesign/blob/master/%E5%AF%B9%E8%AF%9D%E6%9C%BA%E5%99%A8%E4%BA%BA%E6%8A%80%E6%9C%AF%E7%AE%80%E4%BB%8B%EF%BC%9A%E9%97%AE%E7%AD%94%E7%B3%BB%E7%BB%9F%E3%80%81%E5%AF%B9%E8%AF%9D%E7%B3%BB%E7%BB%9F%E4%B8%8E%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA/README.md
[20] https://github.com/madawei2699/myGPTReader/blob/main/README-CN.md
