# flake8: noqa

################################### Old Functions I Don't Want to Delete ###################################
# I don't remember what this does and I'm scared to delete it
@confidence(45)
@dependsOnPackage('tkinter', _as='tk')
@dependsOnPackage('tkinter.ttk', _as='ttk')
@dependsOnPackage('contextlib', 'redirect_stdout')
@dependsOnPackage('ttkthemes')
def stylenameElementOptions(stylename):
    '''Function to expose the options of every element associated to a widget
       stylename.'''
    with open('tmp.del', 'a') as f:
        with redirect_stdout(f):
            print('\n-----------------------------------------------------------------------------\n')
            try:
                # Get widget elements
                style = ttk.Style()
                layout = str(style.layout(stylename))
                print('Stylename = {}'.format(stylename))
                print('Layout    = {}'.format(layout))
                elements=[]
                for n, x in enumerate(layout):
                    if x=='(':
                        element=""
                        for y in layout[n+2:]:
                            if y != ',':
                                element=element+str(y)
                            else:
                                elements.append(element[:-1])
                                break
                print('\nElement(s) = {}\n'.format(elements))
                # Get options of widget elements
                for element in elements:
                    print('{0:30} options: {1}'.format(
                        element, style.element_options(element)))
            except tk.TclError:
                print('_tkinter.TclError: "{0}" in function'
                    'widget_elements_options({0}) is not a regonised stylename.'
                    .format(stylename))

    # for i in ['TButton', 'TCheckbutton', 'TCombobox', 'TEntry', 'TFrame', 'TLabel', 'TLabelFrame', 'TMenubutton', 'TNotebook', 'TPanedwindow', 'Horizontal.TProgressbar', 'Vertical.TProgressbar', 'TRadiobutton', 'Horizontal.TScale', 'Vertical.TScale', 'Horizontal.TScrollbar', 'Vertical.TScrollbar', 'TSeparator', 'TSizegrip', 'Treeview', 'TSpinbox']:
    #     stylenameElementOptions('test.' + i)

    # stylenameElementOptions('me.TButton')

@depricated
def ref(obj):
    return pointer(py_object(obj))

@depricated
def deref(ptr):
    return ptr.contents.value
