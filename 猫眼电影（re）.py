import requests
from requests import RequestException
import re

html_demo = '''
<!DOCTYPE html>

<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if gt IE 9]><!--><html><!--<![endif]-->
<head>
  <title>热映口碑榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//s0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//analytics.meituan.com" />
  <link rel="dns-prefetch" href="//report.meituan.com" />
  <link rel="dns-prefetch" href="//frep.meituan.com" />

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  <script>"use strict";!function(){var i=0<arguments.length&&void 0!==arguments[0]?arguments[0]:"_Owl_",n=window;n[i]||(n[i]={isRunning:!1,isReady:!1,preTasks:[],dataSet:[],use:function(i,t){this.isReady&&n.Owl&&n.Owl[i](t),this.preTasks.push({api:i,data:[t]})},add:function(i){this.dataSet.push(i)},run:function(){var t=this;if(!this.isRunning){this.isRunning=!0;var i=n.onerror;n.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),i&&i.apply(n,arguments)}.bind(this),(n.addEventListener||n.attachEvent)("error",function(i){t.isReady||t.add({type:"resError",data:[i]})},!0)}}},n[i].run())}();</script>
  <script>
  cid = "c_wx6zb55";
  ci = 52;
val = {"subnavId":7};    window.system = {};

  window.openPlatform = '';
  window.openPlatformSub = '';
  window.$mtsiFlag = '0';
  window.NODE_ENV = 'production';

  </script>
  <link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.6b1d782c.css"/>
<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.92a06072.css"/>
  <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/stat.88d57c80.js"></script>
  <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image-2x.8ba7074d.css"/>') }</script>
  <style>
    @font-face {
      font-family: stonefont;
      src: url('//vfile.meituan.net/colorstone/b87efac777b88dee5958d66ec57e15a33436.eot');
      src: url('//vfile.meituan.net/colorstone/b87efac777b88dee5958d66ec57e15a33436.eot?#iefix') format('embedded-opentype'),
           url('//vfile.meituan.net/colorstone/4f1c1fa411e5dce125a34805830b2df42276.woff') format('woff');
    }

    .stonefont {
      font-family: stonefont;
    }
  </style>
  <script>
  var _hmt = _hmt || [];
  (function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?703e94591e87be68cc8da0da7cbd0be2";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
  })();
  </script>
</head>
<body>


<div class="header">
  <div class="header-inner">
          <a href="//maoyan.com" class="logo" data-act="icon-click">猫眼电影</a>
        <div class="city-container" data-val="{currentcityid:52 }">
            <div class="city-selected">
                <div class="city-name">
                  无锡
                  <span class="caret"></span>
                </div>
            </div>
            <div class="city-list" data-val="{ localcityid: 52 }">
                <div class="city-list-header">定位城市：<a class="js-geo-city" data-ci="52">无锡</a></div>
                
            </div>
        </div>


        <div class="nav">
            <ul class="navbar">
                <li><a href="/" data-act="home-click"  >首页</a></li>
                <li><a href="/films" data-act="movies-click" >电影</a></li>
                <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li> 
                <li><a href="http://www.gewara.com">演出</a></li>
                
                <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
                <li><a href="/news" data-act="hotNews-click" >热点</a></li>
                <li><a href="/edimall"  >商城</a></li>
            </ul>
        </div>

        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu no-login-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
    
  </div>
</div>
<div class="header-placeholder"></div>

<div class="subnav">
  <ul class="navbar">
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:7}"
          data-state-val="{subnavId:7}"
          class="active" href="javascript:void(0);"
      >热映口碑榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:6}"
          href="/board/6"
      >最受期待榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:1}"
          href="/board/1"
      >国内票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:2}"
          href="/board/2"
      >北美票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:4}"
          href="/board/4"
      >TOP100榜</a>
    </li>
  </ul>
</div>


    <div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2021-10-23<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将昨日国内热映的影片，按照评分从高到低排列取前10名，每天上午10点更新。相关数据来源于“猫眼专业版”及“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1413319" title="1950他们正年轻" class="image-link" data-act="boarditem-click" data-val="{movieId:1413319}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/2a699851bed2717ebf37da80d3e2fb901350390.jpg@160w_220h_1e_1c" alt="1950他们正年轻" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1413319" title="1950他们正年轻" data-act="boarditem-click" data-val="{movieId:1413319}">1950他们正年轻</a></p>
        <p class="star">
                主演：薛英杰,叶发坤,雍卫太
        </p>
<p class="releasetime">上映时间：2021-09-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/257706" title="长津湖" class="image-link" data-act="boarditem-click" data-val="{movieId:257706}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/0e81560dc9910a6a658a82ec7a054ceb5075992.jpg@160w_220h_1e_1c" alt="长津湖" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/257706" title="长津湖" data-act="boarditem-click" data-val="{movieId:257706}">长津湖</a></p>
        <p class="star">
                主演：吴京,易烊千玺,段奕宏
        </p>
<p class="releasetime">上映时间：2021-09-30</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/1417305" title="我和我的父辈" class="image-link" data-act="boarditem-click" data-val="{movieId:1417305}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/mmdb/ceab1c48a4a1e2d9fe941757ee2f5152256864.jpg@160w_220h_1e_1c" alt="我和我的父辈" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1417305" title="我和我的父辈" data-act="boarditem-click" data-val="{movieId:1417305}">我和我的父辈</a></p>
        <p class="star">
                主演：吴京,章子怡,徐峥
        </p>
<p class="releasetime">上映时间：2021-09-30</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/1328693" title="五个扑水的少年" class="image-link" data-act="boarditem-click" data-val="{movieId:1328693}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/mmdb/81ca765741e6bbb430d213f736a50c964487800.jpg@160w_220h_1e_1c" alt="五个扑水的少年" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1328693" title="五个扑水的少年" data-act="boarditem-click" data-val="{movieId:1328693}">五个扑水的少年</a></p>
        <p class="star">
                主演：辛云来,冯祥琨,李孝谦
        </p>
<p class="releasetime">上映时间：2021-10-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/1356063" title="峰爆" class="image-link" data-act="boarditem-click" data-val="{movieId:1356063}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/mmdb/e93bb766c6fe26424f6f9609d99768de3910793.jpg@160w_220h_1e_1c" alt="峰爆" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1356063" title="峰爆" data-act="boarditem-click" data-val="{movieId:1356063}">峰爆</a></p>
        <p class="star">
                主演：朱一龙,黄志忠,陈数
        </p>
<p class="releasetime">上映时间：2021-09-17</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/1368394" title="保家卫国——抗美援朝光影纪实" class="image-link" data-act="boarditem-click" data-val="{movieId:1368394}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/5dd1ad333dd83d8498aa9450b12bc0fd3332732.jpg@160w_220h_1e_1c" alt="保家卫国——抗美援朝光影纪实" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1368394" title="保家卫国——抗美援朝光影纪实" data-act="boarditem-click" data-val="{movieId:1368394}">保家卫国——抗美援朝光影纪实</a></p>
        <p class="star">
                主演：张涵予,王瑜本,王忠礼
        </p>
<p class="releasetime">上映时间：2020-10-25</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/1236912" title="远去的牧歌" class="image-link" data-act="boarditem-click" data-val="{movieId:1236912}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/c0433df2d57619a0a6774106feb124524057271.jpg@160w_220h_1e_1c" alt="远去的牧歌" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1236912" title="远去的牧歌" data-act="boarditem-click" data-val="{movieId:1236912}">远去的牧歌</a></p>
        <p class="star">
                主演：海拉提·哈木,玛尔江.巴依吐肯,丽娜·夏侃
        </p>
<p class="releasetime">上映时间：2018-09-11</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/1360088" title="关于我妈的一切" class="image-link" data-act="boarditem-click" data-val="{movieId:1360088}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/c9f8427157e1a00c5d0c285807332c3e4925236.jpg@160w_220h_1e_1c" alt="关于我妈的一切" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1360088" title="关于我妈的一切" data-act="boarditem-click" data-val="{movieId:1360088}">关于我妈的一切</a></p>
        <p class="star">
                主演：徐帆,张婧仪,许亚军
        </p>
<p class="releasetime">上映时间：2021-09-19</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/1298314" title="皮皮鲁与鲁西西之罐头小人" class="image-link" data-act="boarditem-click" data-val="{movieId:1298314}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/b862a85e39d28201838f98961e09d7191298056.jpg@160w_220h_1e_1c" alt="皮皮鲁与鲁西西之罐头小人" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1298314" title="皮皮鲁与鲁西西之罐头小人" data-act="boarditem-click" data-val="{movieId:1298314}">皮皮鲁与鲁西西之罐头小人</a></p>
        <p class="star">
                主演：洪悦熙,庄则熙,田雨
        </p>
<p class="releasetime">上映时间：2021-09-30</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/1331267" title="一点就到家" class="image-link" data-act="boarditem-click" data-val="{movieId:1331267}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/c16b0a68f95d884d428f339f8eacce834410200.jpg@160w_220h_1e_1c" alt="一点就到家" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1331267" title="一点就到家" data-act="boarditem-click" data-val="{movieId:1331267}">一点就到家</a></p>
        <p class="star">
                主演：刘昊然,彭昱畅,尹昉
        </p>
<p class="releasetime">上映时间：2020-10-04</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
    </div>
</div>

    </div>

<div class="footer">
  <p class="friendly-links">
    关于猫眼 :
    <a href="http://ir.maoyan.com/s/index.php#pageScroll0" target="_blank">关于我们</a>
    <span></span>
    <a href="http://ir.maoyan.com/s/index.php#pageScroll1" target="_blank">管理团队</a>
    <span></span>
    <a href="http://ir.maoyan.com/s/index.php#pageScroll2" target="_blank">投资者关系</a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    友情链接 :
    <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan" target="_blank">美团网</a>
    <span></span>
    <a href="http://www.gewara.com" data-query="utm_source=wwwmaoyan">格瓦拉</a>
    <span></span>
    <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan" target="_blank">美团下载</a>
    <span></span>
    <a href="https://www.huanxi.com" data-query="utm_source=maoyan_pc" target="_blank">欢喜首映</a>
  </p>
  <p class="friendly-links">
    商务合作邮箱：v@maoyan.com
    客服电话：10105335
    违法和不良信息/涉未成年人有害信息举报电话：4006018900
  </p>
  <p class="friendly-links">
    用户举报/涉未成年人有害信息举报邮箱：tousujubao@meituan.com
    舞弊线索举报邮箱：wubijubao@maoyan.com
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/1" target="_blank">中华人民共和国增值电信业务经营许可证 京B2-20190350</a>
    <span></span>
    <a href="/about/licence/4" target="_blank">营业性演出许可证 京演（机构）（2019）4094号</a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/3" target="_blank">广播电视节目制作经营许可证 （京）字第08478号</a>
    <span></span>
    <a href="/about/licence/2" target="_blank">网络文化经营许可证 京网文（2019）3837-369号 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/rules/agreement" target="_blank">猫眼用户服务协议 </a>
    <span></span>
    <a href="/rules/rule" target="_blank">猫眼平台交易规则总则 </a>
    <span></span>
    <a href="/rules/privacy" target="_blank">隐私政策 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备
      11010102003232号</a>
    <span></span>
    <a href="http://beian.miit.gov.cn/" target="_blank">京ICP备16022489号-1</a>
  </p>
  <p>北京猫眼文化传媒有限公司</p>
  <p>
    &copy;<span class="my-footer-year">2016</span>
    猫眼电影 maoyan.com</p>
  <div class="certificate">
    <a href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/350CF8BCA8416C4FE0530140A8C0957E"
      target="_blank">
      <img src="https://p0.meituan.net/moviemachine/e54374ccf134d1f7b2c5b075a74fca525326.png" />
    </a>
    <a href="/about/licence/5" target="_blank">
      <img src="https://p1.meituan.net/moviemachine/805f605d5cf1b1a02a4e3a5e29df003b8376.png" />
    </a>
    <a href="https://www.12377.cn" target="_blank">
      <img src="https://p0.meituan.net/scarlett/3cd2a9b7dc179531d20d27a5fd686e783787.png" />
    </a>
  </div>
</div>

    <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.7.11.js"></script>
    <script>
      Owl.start({
        project: 'com.sankuai.movie.fe.mywww',
        pageUrl: location.href.split('?')[0].replace(/\/\d+/g, '/:id'),
        devMode: false
      })
    </script>
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-shim.bbad933f.js"></script><![endif]-->
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-sham.d6ea26f4.js"></script><![endif]-->
    <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.c5e8f9fe.js"></script>
<script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.be8ae70e.js"></script>
</body>
</html>'''


def get_one_page(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.310"
    }
    try:
        response = requests.get(url, headers=head)
        response.encoding = "utf-8"
        if response.status_code == 200:
            return response.text
        return None
    except requests.RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(r'.*?<dd>.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?'
                         r'<p class="releasetime">上映时间：(.*?)<.*?'
                         r'<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'name': item[0],
            'star': item[1].strip(),
            'time': item[2],
            'score': item[3] + item[4],
        }


def main():
    url = "https://maoyan.com/board"
    # html = get_one_page(url)
    for item in parse_one_page(html_demo):
        print(item)


if __name__ == '__main__':
    main()
