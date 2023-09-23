#!/usr/bin/env python3
from bot import CMD_SUFFIX

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror{CMD_SUFFIX}', f'tgm{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror{CMD_SUFFIX}', f'tgm{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl{CMD_SUFFIX}', f'ty{CMD_SUFFIX}']
        self.LeechCommand = [f'leech{CMD_SUFFIX}', f'tl{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech{CMD_SUFFIX}', f'tql{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech{CMD_SUFFIX}', f'tyl{CMD_SUFFIX}']
        self.CloneCommand = [f'clone{CMD_SUFFIX}', f'tcl{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del{CMD_SUFFIX}'
        self.CancelMirror = [f'cancel{CMD_SUFFIX}', f'can{CMD_SUFFIX}']
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', f'call{CMD_SUFFIX}']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = [f'search{CMD_SUFFIX}', f'src{CMD_SUFFIX}']
        self.StatusCommand = [f'status{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddSudoCommand = [f'addsudo{CMD_SUFFIX}', f'as{CMD_SUFFIX}']
        self.RmSudoCommand = [f'rmsudo{CMD_SUFFIX}', f'rs{CMD_SUFFIX}']
        self.PingCommand = [f'ping{CMD_SUFFIX}', 'pingall', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', 'restartall', f'r{CMD_SUFFIX}']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = [f'clearlocals{CMD_SUFFIX}', f'cl{CMD_SUFFIX}']
        self.BotSetCommand = [f'bsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest{CMD_SUFFIX}', f'spt{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.AddImageCommand = [f'addimg{CMD_SUFFIX}', f'ai{CMD_SUFFIX}']
        self.ImagesCommand = [f'images{CMD_SUFFIX}', f'img{CMD_SUFFIX}']
        self.MediaInfoCommand = f'mediainfo{CMD_SUFFIX}'
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', 'broadcastall', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()