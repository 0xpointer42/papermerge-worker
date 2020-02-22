

"""
OCR operations are per page. Cut/Paste/Delete/Reorder are per page as well.
So it does not make sense to rerun such a heavy operation as OCR again, instead
we can do some magic tricks (copy them from one location to another)
on already extracted txt and hocr files.

OcrMigrate class takes care of this sort of txt/hocr files moves.
"""


def get_pagecount(ep):
    """
    Returns total number of pages for this endpoint
    """
    pass


class OcrMigrate:
    """
    Insead of running again OCR operation on changed document AGAIN
    (e.g. after pages 2 and 3 were deleted)
    text files which are result of first (and only!) OCR are moved
    (moved = migrated) inside new version's folder.
    Basically migrate/move files instead of rerunning OCR operation.

    For each affected page (page_x), following files will need to be migrated:
        * <version>/pages/page_x.txt
        * <version>/pages/page_x/50/*.hocr
        * <version>/pages/page_x/75/*.hocr
        * <version>/pages/page_x/100/*.hocr
        * <version>/pages/page_x/125/*.hocr
        from <old_version> to <new_version>

    Which pages are affected depends on the operation.
    """

    def __init__(self, src_ep, dst_ep):
        self.src_ep = src_ep
        self.dst_ep = dst_ep

    def get_assigns_after_delete(self, total_pages, deleted_pages):
        """
        given total pages and a list of deleted pages - returns
        a list of assignations of pages:
            [new_version_page_num, old_version_page_num]
        Example 1:
        total_pages: 6
        deleted_pages: [1, 2]
        returns: [
            [[1, 3],  [2, 4], [3, 5], [4, 6]]
            # page #1 gets info from prev page #3
            # page #2 ... #4
            ...
            # page #4 ... #6
        ]

        Example 2:
        total pages: 5
        deleted_pages [1, 5]
        returns: [
            [[1, 2], [2, 3], [3, 4]
        ]

        Example 3:
        total pages: 5
        deleted_pages [2, 3]
        returns: [
            [[1, 1], [2, 4], [3, 5]
            # page #1 stays unaffected
            # page #2 gets the info from page number 4
            # page #3 gets info from page #5
        ]
        """
        pass

    def migrate_delete(self, deleted_pages):
        pass