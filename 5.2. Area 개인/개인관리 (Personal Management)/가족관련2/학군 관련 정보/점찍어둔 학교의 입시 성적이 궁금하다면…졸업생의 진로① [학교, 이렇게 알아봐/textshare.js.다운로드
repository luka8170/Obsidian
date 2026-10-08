(function ($) {

    /**
     * getStringFromByteLength
     * Cut the string as much as Byte and bring it.
     */
    String.prototype.getStringFromByteLength = function( byteLength ) {
        const contents = this;
        let str_character;
        let int_char_count = 0;
        let int_contents_length = contents.length;
    
        let returnValue = '';
    
        for (k = 0; k < int_contents_length; k++) {
            str_character = contents.charAt(k);
            if (escape(str_character).length > 4)
                int_char_count += 2;
            else
                int_char_count++;
    
            if ( int_char_count > byteLength ) {
                break;
            }
            returnValue += str_character;
        }
        return returnValue;
    }
    
    /**
     * textShare object
     * <textShare> tag Under <body> position absolute,
     */
    window.textShare = function (options) {
        var _this = this;
        options = options || {};
        this.options = {
            articleBodyId : options.articleBodyId || 'article_txt',
            contextBoxId : options.contextBoxId || 'txt_share',
            boxPosition : options.boxPosition || 'center'
        }
       
        /**
         * detectIEEdge
         * @returns version of IE/Edge or false, if browser is not a Microsoft browser
         */
        this.detectIEEdge = function() {
            var ua = window.navigator.userAgent;                 
            var msie = ua.indexOf('MSIE ');
            if (msie > 0) {
                // IE 10 or older => return version number
                return parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
            }

            var trident = ua.indexOf('Trident/');
            if (trident > 0) {
                // IE 11 => return version number
                var rv = ua.indexOf('rv:');
                return parseInt(ua.substring(rv + 3, ua.indexOf('.', rv)), 10);
            }

            var edge = ua.indexOf('Edge/');
            if (edge > 0) {
            // Edge => return version number
            return parseInt(ua.substring(edge + 5, ua.indexOf('.', edge)), 10);
            }

            // other browser
            return false;
        }
        
        /**
         * device info
         */
        this.device = new (function () {
            var ua = window.navigator.userAgent;
            this.isMobile = false;                
            if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(ua) 
                || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(ua.substr(0,4))) { 
                this.isMobile = true;
            }                   
            this.isTablet = this.isMobile && !/mobile/i.test(ua);
            this.isPC = !this.isMobile && !this.isTablet;
            this.isiOS = /ipad|iphone|ipod/i.test(ua);
            this.isAnd = /android/i.test(ua);
            this.msieInfo = _this.detectIEEdge();
            this.isIEEdge = false;
            if ( this.msieInfo != false )
            {
                this.isIEEdge = true ;
                this.isIEEdgeVersion = this.msieInfo ;
            }
        })();

        /**
        * Verify that the text selection is valid
        */
        this.isValid = function() {                
            var start = _this.range.startContainer;
            var end = _this.range.endContainer;               
            $isTrue1 = start.parentElement.id === _this.options.articleBodyId && end.parentElement.id === _this.options.articleBodyId ;
            $isTrue2 = start.parentElement.parentElement.id === _this.options.articleBodyId && end.parentElement.parentElement.id === _this.options.articleBodyId ;
            if ( $isTrue1 || $isTrue2 ) //only two-depth is valid
            {
                if (_this.selection.toString().trim().length < 1) {
                    _this.removeSelection();
                    return false;
                }
                else return true;
            }
            else 
            {
                _this.removeSelection();
                return false;
            }
        };

        
         /**
        * object -> url queryString convert
        */
        this.objectToQueryString = function(obj) {
            var str = [];
            for (var param in obj) {
                if (obj.hasOwnProperty(param)) 
                {
                    str.push(encodeURIComponent(param) + "=" + encodeURIComponent(obj[param]));
                }
            }
            return '?' + str.join("&");
        }
        
        /**
         * get meta tag value
         * 
         * code example:
         * <scipt>
         * getMetaValue('og:url');
         * </scipt>
         */
        this.getMetaValue = function (name) {
            var metaTag = $('meta') ; 
            var $content = '';
            metaTag.each(function () {
                $meta = $(this);            
                if ($meta.attr('name') !== undefined && $meta.attr('name') === name) {
                    $content = $meta.attr('content');
                    return ;
                }
                else if ($meta.attr('property') !== undefined && $meta.attr('property') === name) {
                    $content = $meta.attr('content');
                    return ;
                }
            });

            return $content ;
        };

        /**
        * delete selection
        */
        this.removeSelection = function() {
            delete _this.selection;
            delete _this.range;
        }
     
        /**
        * change selection
        */
        this.selectionChange = function (e) {
            try {
                _this.selection = window.getSelection();
                $contextBox = $("#"+_this.options.contextBoxId) ;
                if (_this.selection.type !== 'None') {
                    _this.range = _this.selection.getRangeAt(0).cloneRange();                
                    if (_this.selection.toString().trim().length < 1) {
                        _this.hideContextBox();
                    }
                }        
            } catch (error) {
                _this.removeSelection();         
            }
        };
        /**
        * isElementHidden 
        */
        this.isElementHidden = function($ele) {            
            if ( $ele.css("visibility") === "hidden") {
                return true;
            } else {
                return false;
            }
        };

        /**
        * mouseup event handler
        */
        this.mouseUp = function (e) {
            $contextBox = $("#"+_this.options.contextBoxId) ;
            if ( _this.isElementHidden($contextBox) && _this.selection && _this.selection.toString().trim().length > 0) {
                if ( _this.isValid() ) _this.showContextBox();
            } 
        };

        /**
        * show contextBox
        * calculate the location of a box
        */
        this.showContextBox = function () {    
            $contextBox = $("#"+_this.options.contextBoxId) ;   
            $articleBody = $("#"+_this.options.articleBodyId) ;  
             
            var bodyOffset = $articleBody.offset();
            var bodyWid = $articleBody.width();
            var bodyRect = $articleBody[0].getBoundingClientRect(); //viewport-based Body area Information                    
           
            var areaRects = _this.range.getClientRects(); //viewport-based text block areas  Information (array line block info)
            var areaRect = areaRects[areaRects.length - 1]; //last line block  
           
            var ctxboxWid = $contextBox.width();
            var ctxBoxTop = - bodyRect.top + bodyOffset.top + areaRect.top + areaRect.height + 10; 
            var ctxboxLeft = 0 ;
            switch (_this.options.boxPosition ) {
                case "center":
                    ctxboxLeft = areaRect.right - (areaRect.width / 2) - ( ctxboxWid / 2 ) ; //ceter
                    break;
                case "rcenter": 
                    ctxboxLeft = areaRect.right - ( ctxboxWid / 2 ) ;              
                    break;
                case "right":  
                    ctxboxLeft = areaRect.right - ctxboxWid ;            
                    break;
                default:
                    console.log("position종류 : center(선택영역의 가운데 기본값), rcenter(선택영영의 오른쪽끝이 박스의 중심), right(박스,선택영역 오른쪽 끝 맞춤) ");
                    break;
            }

            if ( bodyOffset.left > ctxboxLeft ) {   
                ctxboxLeft = bodyOffset.left + 10 ;
            }
            else if ( bodyOffset.left + bodyWid < ctxboxLeft + ctxboxWid )
            {         
                ctxboxLeft = bodyOffset.left + bodyWid - ctxboxWid - 10 ;
            }
            $contextBox.css({ left: ctxboxLeft, top: ctxBoxTop, visibility: 'visible' });
        };

        /**
        * hide contextBox
        */
        this.hideContextBox = function () {                   
            $("#"+_this.options.contextBoxId).css('visibility', 'hidden'); 
        };

        $(document).on('mouseup', '#'+_this.options.contextBoxId, (function (e){
            if ( $(this).length )
            {
                if($contextBox.has(e.target).length === 0 && !_this.isElementHidden($contextBox) ){
                    e.preventDefault();
                    e.stopPropagation();
                    _this.hideContextBox();
                }
            }
        }));

         /**
         * share object with facebook , twitter, kakaotalk function    
         */
        this.share = new (function () {
            var _s = this ;
            this.config = {
                kakaotalkKey: '6158b6b574f5c2663c58e3d4bc6f0cb9',   
                originUrl: window.location.origin + window.location.pathname,
                ogTitle: _this.getMetaValue('og:title'),
                ogImage: _this.getMetaValue('og:image'),
                ogDesc: _this.getMetaValue('og:description'),
                twTitle: _this.getMetaValue('twitter:title'),
                twImage: _this.getMetaValue('twitter:image:src'),
                twDesc: _this.getMetaValue('twitter:description'),
                fbUtm: '?utm_source=facebook&utm_medium=share&utm_campaign=article_share_fb',
                twUtm: '?utm_source=twitter&utm_medium=share&utm_campaign=article_share_tw',
                ktUtm: '?utm_source=kakao&utm_medium=share&utm_campaign=article_share_kt',
            };

            /**
             * facebook share event
             */
            this.facebook = function (options) {
                options = options || {};    
                var url = _s.config.originUrl + _s.config.fbUtm ;
                var snsUrl = 'https://www.facebook.com/sharer/sharer.php';
                var paramObj = { u: url };
                var openUrl = snsUrl + _this.objectToQueryString(paramObj);           
                window.open(openUrl, '_SNS', 'width=860, height=500, scrollbars=yes, resizable=yes');           
            };

            /**
             * twitter share event
             */
            this.twitter = function (options) {
                options = options || {};
                var title = ( options.title || _s.config.twTitle ).getStringFromByteLength(230) + '...' ;
                var url =  _s.config.originUrl + _s.config.twUtm ;
                var snsUrl = 'https://twitter.com/intent/tweet';
                var paramObj = { text: title, url: url };
                var openUrl = snsUrl + _this.objectToQueryString(paramObj);
                window.open(openUrl, '_SNS', 'width=860, height=500, scrollbars=yes, resizable=yes');           
            };

            /**
             * kakaotalk share event
             */
            this.kakaotalk = function (options) {
                options = options || {};
                var url = _s.config.originUrl + _s.config.ktUtm ;             

                if ( window.Kakao )
                {
                    if ( !window.Kakao.isInitialized()) window.Kakao.init(_s.config.kakaotalkKey) ;

                    if (_s.config.ogTitle && _s.config.ogTitle !== '') {
                        window.Kakao.Link.sendDefault({
                            objectType: 'feed',
                            content: {
                                title: options.title || _s.config.ogTitle,
                                description: ( options.desc || _s.config.ogDesc || _s.config.ogTitle ).substr(0,60) + '...' ,
                                imageUrl: options.imageUrl || _s.config.ogImage,
                                link: {
                                    mobileWebUrl: url,
                                    webUrl: url
                                }
                            }
                        });
                    }    
                }              
            };

            $(document).on('click',"#"+_this.options.contextBoxId + " a",function (e) {
                e.preventDefault();
                var snsType = $(this).data('type');
                var title = _this.selection.toString() ;
                var descTitle = _this.getMetaValue('og:title') ;
                switch (snsType) {
                    case 'facebook':
                        _s.facebook();
                        break;
                    case 'twitter':
                        _s.twitter( { title : title } );
                        break;
                    case 'kakaotalk':
                        _s.kakaotalk( { title : title, desc : descTitle } );
                        break;
                    default:
                        return;
                }
            }) ;

        })();

        document.addEventListener('selectionchange', _this.selectionChange);
        document.addEventListener('mouseup', _this.mouseUp);
    };

})(window.jQuery);