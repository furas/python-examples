
# House:
    http://plahou-01.cdn.eurozet.pl:8208/;stream.nsv?seed=391.58846251666546
    
# Progressive House:
    http://plapro-01.cdn.eurozet.pl:8214/;stream.nsv?seed=26287.59954124689
    http://plapro-01.cdn.eurozet.pl:8214/index.html

# Oldschool:
    http://plaold-01.cdn.eurozet.pl:8212/;stream.nsv?seed=17491.683061234653

# Pop/R'n'B:
    http://plarnb-01.cdn.eurozet.pl:8216/;stream.nsv?seed=10058.084819465876
        
# Trance:
    http://platra-01.cdn.eurozet.pl:8218/;stream.nsv?seed=23805.67128304392
        
# Alternative:
    http://plaalt-01.cdn.eurozet.pl:8210/;stream.nsv?seed=8542.433772236109

# Chill Out
    http://plachi-01.cdn.eurozet.pl:8204/;stream.nsv?seed=19347.927449271083
#------
    
http://rds.eurozet.pl/reader/var/plaalt_new.json

Markus Schulz:
    http://redir.atmcdn.pl/http/o2/Eurozet/audio/57/2ad3cd2d868995ade6b8593afc9cc298/336670c9f430a130d381f03f7ae78077.mp3
    http://n-4-1.dcs.redcdn.pl/dcs/o2/Eurozet/audio/57/2ad3cd2d868995ade6b8593afc9cc298/336670c9f430a130d381f03f7ae78077.mp3

#---------------------------------------------------------------------- 

view-source:http://www.planeta.fm/sluchaj/online/Planeta-Oldskul.html
    <script type="text/javascript" src="http://gfx.planeta.fm/externals/sluchaj/config/Planeta-Oldskul.js"></script>

http://gfx.planeta.fm/externals/sluchaj/config/Planeta-Oldskul.js

'''
Channel = {
    // konfiguracja kanaÅ‚u
    name    : 'Planeta Oldskul',
    emitter : 'plaold_new',
    stream  : [
        'http://plaold-01.cdn.eurozet.pl:8212', 'http://plaold-02.cdn.eurozet.pl:8212'
    ],
    
    // konfiguracja statystyk
    google_analytics : {
        tracker             : ['UA-56223553-1']
    },
    gemius_audience : {
        identifier          : ['.ReQpCMtm7gP_1xrLbRdX4ZirqwF_pt_Hl7ux5E5TXT.I7'],
        time_identifier     : ['bJs6FtycL9Qh3UBko6pUZPWp7DnFVSvdYqzMwZCY7jP.X7']
    },
    gemius_traffic : {
        identifier          : ['chrlRstRLdhyc5Ol.dH_grbuHPx82uNGLY41qAoOFxr.j7']
    },
    gemius_stream : {
        materialIdentifier  : 'PlanetaFM-Oldskul',
        customPackage       : [
            {name:  "R_KANAL", value: "muzyczny"}
        ],
        identifier          : 'ogiVHb9BEQ9eQyIayp5U3IXz7A7FOXhFYwPEAFnUlz3.h7'
    },
    sensic_stream: {
        contentId           : "planeta_audio_on_demand",
    },
    // konfiguracja reklam
    googletag: {
        name                : '/4350995/PlanetaFM_player',
        size                : [468, 60],
        wrapper             : 'div-gpt-ad-1342693778027-0'
    }
}
'''

#---------------------------------------------------------------------- 

'''
/*!
 * ePlayer JavaScript Library v2.0
 * 
 * @author Tomasz Pietrzak <tomasz.pietrzak@eurozet.pl>
 */
(function(window, undefined) {
    
    /**
     * Drzewo wykonanych aplikacji.
     * 
     * @access private
     */
    var _applicationList = null;
    
    /**
     * ZarzÄ…dzanie konfiguracjÄ….
     * 
     * @type type
     */
    var Config = {
        /**
         * Name
         */
        name: 'eplayer-online',
        
        /**
         * Flaga czy zainicjowane
         * @type type
         */
        initialized: false,
        
        /**
         * Date do synchronizacji
         */
        time: {
            url     : 'http://rds.eurozet.pl/reader/time.php',
            synchro : 0,
            timeout : null,
            minimal : 30 * 1000
        },
        
        /**
         * ÅšcieÅ¼ka do okÅ‚adki
         */
        cover: '/images/default-album-cover_%dx%d.png',
        
        /**
         * RDS
         */
        rds: 'http://rds.eurozet.pl/reader/var/%s.json',
        
        /**
         * ZarzÄ…dzanie danymi
         * @type type
         */
        storage: {
            'now'   : 'now',
            'next1' : 'presently',
            'next2' : 'presently'
        }
    };
    
    /**
     * Storage
     */
    var Storage = {
        now: [],
        presently: []
    };
    
    /**
     * ZarzÄ…dzenie RDS'e
     */
    var RDS = {
        /**
         * Inicjowanie RDS'a
         */
        init: function() {
            // ustawianie listner'a na poprawne pobranie danych
            Config.time.timeout = window.setTimeout(RDS.update, 5 * 1000);
            
            // pobieranie danych
            $.ajax({
                url             : Config.time.url,
                dataType        : 'jsonp',
                jsonp           : false,
                jsonpCallback   : 'rdsTime',
                crossDomain     : true,
                success         : function(serverTime) {
                    // wyÅ‚Ä…cz listner
                    window.clearTimeout(Config.time.timeout);
                    // rÄ™czka korekta rÃ³Å¼nicy w czasie
                    serverTime -= 5 * 60 - 28;
                    // oblicz rÃ³Å¼nicÄ™ w czasie
                    var localTime = Math.ceil(new Date().getTime()/1000);
                    // zapis danych
                    Config.time.synchro = serverTime - localTime;
                    // uruchamianie pobieranie danych z RDS'a
                    RDS.update();
                }
            });
            
            // aktywacja eventÃ³w
            RDS.events();
        },
        /**
         * Pobieranie danych z systemu nadawczego.
         * @returns {undefined}
         */
        update: function() {
            // pobieranie danych
            $.ajax({
                url             : Config.rds.replace('%s', Channel.emitter),
                xhrFields       : {withCredentials: true},
                dataType        : 'jsonp',
                jsonp           : false,
                jsonpCallback   : 'rdsData',
                success         : function(rdsData) {
                    // zmieniÅ‚ siÄ™ trwajÄ…cy utwÃ³r
                    var hasChange = true;
                    
                    // walidacja odebranych danych
                    if (Storage.now.length > 0 && rdsData.now) {
                        // dane sÄ… w storage'u i rds'ie
                        var unique = rdsData.now.artist + ' ' + rdsData.now.title;
                        if (Storage.now[0].unique === unique) {
                            hasChange = false;
                        }
                    }
                    
                    // zmiana danych (przegerowanie Storage'a)
                    if (hasChange) {
                        if (Storage.now.length > 0)
                            // uruchom VAST (midroll)
                            ePlayer_Managment.exec('ePlayer_Vast', 'execute', 'midroll');

                        // czyszczenie danych w Storage'u
                        Storage = {now: [], presently: []};

                        // aktualizacja danych w pamiÄ™ci
                        for(key in Config.storage) {
                            if (rdsData[key]) {
                                var storage = {
                                    unique      : rdsData[key].artist + ' ' + rdsData[key].title,
                                    artistName  : rdsData[key].artist,
                                    artistUrl   : null,
                                    trackName   : rdsData[key].title,                               
                                    trackUrl    : null,
                                    albumCover  : null,
                                    start       : rdsData[key].startDate?(Math.ceil(Date.parse(rdsData[key].startDate.replace(' ', 'T'))/1000) - Config.time.synchro):null,
                                    end         : rdsData[key].endDate  ?(Math.ceil(Date.parse(rdsData[key].endDate.replace(' ', 'T'))/1000) - Config.time.synchro):null
                                }

                                if (rdsData[key].details)
                                {
                                    storage.artistName    = rdsData[key].details.artistName;
                                    storage.artistUrl     = '/' + rdsData[key].details.artistUrl;

                                    storage.trackName     = rdsData[key].details.trackName;
                                    storage.trackUrl      = '/' + rdsData[key].details.albumUrl;

                                    if (rdsData[key].details.albumCover && rdsData[key].details.albumCover.medium) {
                                        storage.albumCover    = rdsData[key].details.albumCover.medium;
                                    }
                                    
                                    if (AppChannel.nourl === true) {
                                        storage.artistUrl   = null;
                                        storage.trackUrl    = null;
                                    }
                                }

                                Storage[Config.storage[key]].push(storage);
                            }
                        }

                        // aktualizacja rds'a
                        try {
                            RDS.upgrade();
                        } catch(e) {
                            ePlayer_Managment.console('ERROR: ePlayer_RDS.upgrade()', Storage);
                        }
                    }
                    
                    // ustawianie flagi na kolejny update
                    var diff    = 0,
                        delay   = Config.time.minimal;
                    
                    if (Storage.presently[0]) {
                        diff = Storage.presently[0].start - Math.ceil(new Date().getTime()/1000)
                    }
                    
                    if (diff > 0 && diff <= (Config.time.minimal/1000)) {
                        delay = (diff + 5) * 1000;
                    }
                    
                    ePlayer_Managment.console('FL: ePlayer_RDS.update(' + Storage.now[0].unique + '; hasChange: ' + hasChange + ')');
                    window.setTimeout(RDS.update, delay);
                }
            });
            
        },
        /**
         * Aktualizacja danych w playerze.
         * @returns {undefined}
         */
        upgrade: function() {
            // aktualizacja
            for(var key in Storage) {
                // usuwanie starych 'Å›mieci'
                $(ePlayer_RDS.getWrapper()).find('.' + key).remove();

                // wrapper
                $(ePlayer_RDS.getWrapper()).append(
                    $('<dl />').addClass(key)
                );
                if (key === 'presently' && Storage.presently.length > 0)
                {
                    $(ePlayer_RDS.getWrapper()).find('.' + key).append(
                        $('<dd />').addClass('header').text('za chwilÄ™:')
                    );
                }
                
                // data
                for(var node in Storage[key])
                {
                    if (node === 'indexOf') {
                        continue;
                    }
                    
                    if (Storage[key][node].albumCover === null)
                        Storage[key][node].albumCover = AppChannel.host.gfx + AppChannel.host.path + Config.cover.split('%d').join((key==='now'?86:31));
                    
                    $(ePlayer_RDS.getWrapper()).find('.' + key).append(
                        $('<dt />').html(
                            $('<img />').attr('alt', Storage[key][node].artistName).attr('src', Storage[key][node].albumCover)
                        )
                    ).append(
                        $('<dd />').html(
                            $('<a />').addClass('artist').addClass(Storage[key][node].artistUrl===null?'unavailable':'')
                                .attr('href', Storage[key][node].artistUrl)
                                .attr('target', '_blank')
                                .attr('title', Storage[key][node].artistName)
                                .text(Storage[key][node].artistName)
                        ).append('<br />').append(
                            $('<a />').addClass('album').addClass(Storage[key][node].trackUrl===null?'unavailable':'')
                                .attr('href', Storage[key][node].trackUrl)
                                .attr('target', '_blank')
                                .attr('title', Storage[key][node].trackName)
                                .text(Storage[key][node].trackName)
                        ).append('<br />')
                    );
                    
                    if( typeof(AppChannel.itunes) === 'object' && AppChannel.itunes.active === true )
                    {   // generowanie iTunes'a
                        ePlayer_Managment.exec('ePlayer_iTunes', 'render', key, node, Storage[key][node].artistName +' - ' + Storage[key][node].trackName);
                    }
                }
            }
        },
        /**
         * Ustawianie event'Ã³w na wczytanych elementach.
         */
        events: function() {
            $(ePlayer_RDS.getWrapper()).find('.now a.artist').live('click', function() {
                var elementUrl = $(this).attr('href');
                _gaq.push(['_trackEvent', 'player', 'player - link - artysta: ' + elementUrl, Channel.name]);
            });
            $(ePlayer_RDS.getWrapper()).find('.now a.album').live('click', function() {
                var elementUrl = $(this).attr('href');
                _gaq.push(['_trackEvent', 'player', 'player - link - album: ' + elementUrl, Channel.name]);
            });

            $(ePlayer_RDS.getWrapper()).find('.presently a.artist').live('click', function() {
                var elementUrl = $(this).attr('href');
                _gaq.push(['_trackEvent', 'player', 'player - link - nast. artysta: ' + elementUrl, Channel.name]);
            });
            $(ePlayer_RDS.getWrapper()).find('.presently a.album').live('click', function() {
                var elementUrl = $(this).attr('href');
                _gaq.push(['_trackEvent', 'player', 'player - link - nast.album: ' + elementUrl, Channel.name]);
            });
        }
    };
    
    /**
     * @acces public
     */
    var ePlayer_RDS = window.ePlayer_RDS  || {
        
        /**
         * Inicjowanie statystyk
         */
        init: function(applicationList)
        {   // ustawianie drzewa wykonywanych aplikacji
            _applicationList = applicationList;

            // przerwij w momencie ponownej prÃ³by inicjowania
            if (Config.initialized) {return;}
            
            // aktualizacja RDS'a
            RDS.init();
            
            // oznacz jako zainicjowane
            Config.initialized = true;
            
            // wyÅ›lij znak koÅ„ca
            ePlayer_Managment.exec('ePlayer_Managment', 'ready', _applicationList);
        },
        
        /**
         * Pobieranie danych z konfiguracji
         */
        getWrapper: function()
        {
            return '#' + Config.name;
        }
    }
    // Å‚ata na starÄ… wersje managment
    ePlayer_RDS.getConfig = ePlayer_RDS.getWrapper;
    // public
    window.ePlayer_RDS = ePlayer_RDS;
})(window);
'''
