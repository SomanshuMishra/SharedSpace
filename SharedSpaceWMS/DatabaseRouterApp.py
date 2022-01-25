class DatabaseRouterApp:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        if model._meta.app_label == 'admin_app':
            return 'default'

        if model._meta.app_label == 'customer_app':
            return 'customer'

        if model._meta.app_label == 'order_app':
            return 'order'

        if model._meta.app_label == 'product_app':
            return 'product'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        if model._meta.app_label == 'admin_app':
            return 'default'

        if model._meta.app_label == 'customer_app':
            return 'customer'

        if model._meta.app_label == 'orders_app':
            return 'order'

        if model._meta.app_label == 'product_app':
            return 'product'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'admin_app' or \
           obj2._meta.app_label == 'admin_app':
           return True

        if obj1._meta.app_label == 'customer_app' or \
           obj2._meta.app_label == 'customer_app':
           return True


        if obj1._meta.app_label == 'orders_app' or \
           obj2._meta.app_label == 'orders_app':
           return True

        if obj1._meta.app_label == 'product_app' or \
           obj2._meta.app_label == 'product_app':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label == 'admin_app':
            return db == 'default'


        if app_label == 'customer_app':
            return db == 'customer'

        if app_label == 'orders_app':
            return db == 'order'

        if app_label == 'orders_app':
            return db == 'product'
        return None