class DBRouter:
    def db_for_read(self, model, **hints):
        appname_split = model._meta.app_label.split('_')
        if len(appname_split) > 1:
            db_cnt = int(appname_split[1])
            return 'database_{}'.format(db_cnt)

    def db_for_write(self, model, **hints):
        appname_split = model._meta.app_label.split('_')
        if len(appname_split) > 1:
            db_cnt = int(appname_split[1])
            return 'database_{}'.format(db_cnt)

    def allow_relation(self, obj1, obj2, **hints):
        appname_split_1 = obj1._meta.app_label.split('_')
        appname_split_2 = obj2._meta.app_label.split('_')
        if len(appname_split_1) > 1 or len(appname_split_2) > 1:
            return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        appname_split = app_label.split('_')
        if len(appname_split) > 1:
            db_cnt = int(appname_split[1])
            return db == 'database_{}'.format(db_cnt)