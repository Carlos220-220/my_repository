from django.http import HttpResponse


def get_num():
    strings = ''
    for c in range(1, 10):
        if c % 2 == 0:
            strings += '<tr class="two">'
        else:
            strings += '<tr class="one">'
        for r in range(1, c + 1):
            strings += ('<td>{}*{}={:<2}</td>'.format(r, c, r * c))
        strings += '</tr>'

    return strings


def tables(request):
    html = '''
    <html>
        <head>
            <style>
                .one{
                    border:1px solid gray;
                    background-color:#f40;
                    color:#424242;
                }
                .two{
                    border:1px solid gray;
                    background-color:#424242;
                    color:#f40;
                }
                tr td{
                    border-radius:20px;
                }
                .active1{
                    color:#fff
                }
            </style>
            <script src="http://libs.baidu.com/jquery/1.9.1/jquery.js"></script>
        </head>
        <body>
            <table>
                %s
            </table>
            <script>
                $('td').mouseover(function(){
                    $(this).addClass('active1').siblings().
                    removeClass('active1');
                })
            </script>
        </body>
    </html>
    ''' % (get_num())
    return HttpResponse(html)

