from tethys_apps.base import TethysAppBase, url_map_maker


class HISTimeSeriesViewer(TethysAppBase):
    """
    Tethys app class for HIS Time Series Viewer.
    """

    name = 'HIS Time Series Viewer'
    index = 'refts_viewer:home'
    icon = 'refts_viewer/images/icon.gif'
    package = 'refts_viewer'
    root_url = 'refts-viewer'
    color = '#e74c3c'
        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='refts-viewer/br/{branch}/res/{res_id}/fn/{filename}',
                           controller='refts_viewer.controllers.restcall'),

                    UrlMap(name='home',
                           url='refts-viewer/',
                           controller='refts_viewer.controllers.home'),

                    UrlMap(name='request_demo',
                           url='refts-viewer/request-demo',
                           controller='refts_viewer.controllers.request_demo'),



        )

        return url_maps