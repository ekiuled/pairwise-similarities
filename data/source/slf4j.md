# File: `StaticLoggerBinder.java`

## Method: `public static final StaticLoggerBinder getSingleton()`

        <!-- META {"entityType": "Method", "entitySignature": "public static final StaticLoggerBinder getSingleton()", "entityFile": "StaticLoggerBinder.java"} -->Return the singleton of this class.
        @return the StaticLoggerBinder singleton

# File: `LocationAwareLogger.java`

## Method: `public void log(Marker marker, String fqcn, int level, String message, Object[] argArray, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void log(Marker marker, String fqcn, int level, String message, Object[] argArray, Throwable t)", "entityFile": "LocationAwareLogger.java"} --><!-- bd02460a-1797-11ea-bef5-333445793454 <=< ACCEPT -->Printing method with support for location information.
        @param marker The marker to be used for this event, may be null.
        @param fqcn The fully qualified class name of the logger instance,
        typically the logger class, logger bridge or a logger wrapper.
        @param level One of the level integers defined in this interface
        @param message The message for the log event
        @param t Throwable associated with the log event, may be null.<!-- ACCEPT >=> bd02460a-1797-11ea-bef5-333445793454 -->

# File: `ILoggerFactory.java`

## Method: `public Logger getLogger(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public Logger getLogger(String name)", "entityFile": "ILoggerFactory.java"} --><!-- a1191774-1797-11ea-b085-333445793454 <=< ACCEPT -->Return an appropriate Logger instance as specified by the
        name parameter.
        If the name parameter is equal to Logger#ROOT_LOGGER_NAME, that is
        the string value "ROOT" (case insensitive), then the root logger of the
        underlying logging system is returned.
        Null-valued name arguments are considered invalid.
        Certain extremely simple logging systems, e.g. NOP, may always
        return the same logger instance regardless of the requested name.
        @param name the name of the Logger to return
        @return a Logger instance<!-- ACCEPT >=> a1191774-1797-11ea-b085-333445793454 -->

# File: `MessageFormatter.java`

## Method: `public static final FormattingTuple format(String messagePattern, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public static final FormattingTuple format(String messagePattern, Object arg)", "entityFile": "MessageFormatter.java"} --><!-- 843dd1de-a242-11e9-90c0-333445793454 <=< ACCEPT -->Performs single argument substitution for the 'messagePattern' passed as
        parameter.
        For example,
        MessageFormatter.format(&quot;Hi {}.&quot;, &quot;there&quot;);
        will return the string "Hi there.".
        @param messagePattern
        The message pattern which will be parsed and formatted
        @param arg
        The argument to be substituted in place of the formatting anchor
        @return The formatted message<!-- ACCEPT >=> 843dd1de-a242-11e9-90c0-333445793454 -->

# File: `StaticLoggerBinder.java`

## Class: `StaticLoggerBinder`

        <!-- META {"entityType": "Class", "entitySignature": "StaticLoggerBinder", "entityFile": "StaticLoggerBinder.java"} -->The binding of org.slf4j.LoggerFactory class with an actual instance of
        ILoggerFactory is performed using information returned by this class.
        This class is meant to provide a dummy StaticLoggerBinder to the slf4j-api module.
        Real implementations are found in  each SLF4J binding project, e.g. slf4j-nop,
        slf4j-log4j12 etc.
        @author Ceki G&uuml;lc&uuml;

# File: `LocationAwareLogger.java`

## Interface: `LocationAwareLogger`

        <!-- META {"entityType": "Interface", "entitySignature": "LocationAwareLogger", "entityFile": "LocationAwareLogger.java"} -->An optional interface helping integration with logging systems capable of
        extracting location information. This interface is mainly used by SLF4J bridges
        such as jcl-over-slf4j, jul-to-slf4j and log4j-over-slf4j or Logger wrappers
        which need to provide hints so that the underlying logging system can extract
        the correct location information (method name, line number).
        @author Ceki Gulcu
        @since 1.3

# File: `ILoggerFactory.java`

## Interface: `ILoggerFactory`

        <!-- META {"entityType": "Interface", "entitySignature": "ILoggerFactory", "entityFile": "ILoggerFactory.java"} -->ILoggerFactory instances manufacture Logger
        instances by name.
        Most users retrieve Logger instances through the static
        LoggerFactory#getLogger(String) method. An instance of of this
        interface is bound internally with LoggerFactory class at
        compile time.
        @author Ceki G&uuml;lc&uuml;

# File: `MessageFormatter.java`

## Method: `public static final FormattingTuple format(final String messagePattern, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public static final FormattingTuple format(final String messagePattern, Object arg1, Object arg2)", "entityFile": "MessageFormatter.java"} --><!-- 843dd1de-a242-11e9-90c0-333445793454 <=< ACCEPT -->Performs a two argument substitution for the 'messagePattern' passed as
        parameter.
        For example,
        MessageFormatter.format(&quot;Hi {}. My name is {}.&quot;, &quot;Alice&quot;, &quot;Bob&quot;);
        will return the string "Hi Alice. My name is Bob.".
        @param messagePattern
        The message pattern which will be parsed and formatted
        @param arg1
        The argument to be substituted in place of the first formatting
        anchor
        @param arg2
        The argument to be substituted in place of the second formatting
        anchor
        @return The formatted message<!-- ACCEPT >=> 843dd1de-a242-11e9-90c0-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        /**
        ILoggerFactory instances manufacture Logger
        instances by name.
        Most users retrieve Logger instances through the static
        LoggerFactory#getLogger(String) method. An instance of of this
        interface is bound internally with LoggerFactory class at
        compile time.
        @author Ceki G&uuml;lc&uuml;
        */
        public interface ILoggerFactory {
        /**
        <!-- a1191774-1797-11ea-b085-333445793454 <=< ACCEPT -->Return an appropriate Logger instance as specified by the
        name parameter.
        If the name parameter is equal to Logger#ROOT_LOGGER_NAME, that is
        the string value "ROOT" (case insensitive), then the root logger of the
        underlying logging system is returned.
        Null-valued name arguments are considered invalid.
        Certain extremely simple logging systems, e.g. NOP, may always
        return the same logger instance regardless of the requested name.
        @param name the name of the Logger to return
        @return a Logger instance<!-- ACCEPT >=> a1191774-1797-11ea-b085-333445793454 -->
        */
        public Logger getLogger(String name);
        }
        (ILoggerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.spi;
        import org.slf4j.Logger;
        import org.slf4j.Marker;
        /**
        An optional interface helping integration with logging systems capable of
        extracting location information. This interface is mainly used by SLF4J bridges
        such as jcl-over-slf4j, jul-to-slf4j and log4j-over-slf4j or Logger wrappers
        which need to provide hints so that the underlying logging system can extract
        the correct location information (method name, line number).
        @author Ceki Gulcu
        @since 1.3
        */
        public interface LocationAwareLogger extends Logger {
        // these constants should be in EventContants. However, in order to preserve binary backward compatibility
        // we keep these constants here
        public final int TRACE_INT = 00;
        public final int DEBUG_INT = 10;
        public final int INFO_INT = 20;
        public final int WARN_INT = 30;
        public final int ERROR_INT = 40;
        /**
        <!-- bd02460a-1797-11ea-bef5-333445793454 <=< ACCEPT -->Printing method with support for location information.
        @param marker The marker to be used for this event, may be null.
        @param fqcn The fully qualified class name of the logger instance,
        typically the logger class, logger bridge or a logger wrapper.
        @param level One of the level integers defined in this interface
        @param message The message for the log event
        @param t Throwable associated with the log event, may be null.<!-- ACCEPT >=> bd02460a-1797-11ea-bef5-333445793454 -->
        */
        public void log(Marker marker, String fqcn, int level, String message, Object[] argArray, Throwable t);
        }
        (LocationAwareLogger.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.impl;
        import org.slf4j.ILoggerFactory;
        /**
        The binding of org.slf4j.LoggerFactory class with an actual instance of
        ILoggerFactory is performed using information returned by this class.
        This class is meant to provide a dummy StaticLoggerBinder to the slf4j-api module.
        Real implementations are found in  each SLF4J binding project, e.g. slf4j-nop,
        slf4j-log4j12 etc.
        @author Ceki G&uuml;lc&uuml;
        */
        public class StaticLoggerBinder {
        /**
        The unique instance of this class.
        */
        private static final StaticLoggerBinder SINGLETON = new StaticLoggerBinder();
        /**
        Return the singleton of this class.
        @return the StaticLoggerBinder singleton
        */
        public static final StaticLoggerBinder getSingleton() {
        return SINGLETON;
        }
        /**
        Declare the version of the SLF4J API this implementation is compiled against.
        The value of this field is modified with each major release.
        */
        // to avoid constant folding by the compiler, this field must *not* be final
        // !final
        public static String REQUESTED_API_VERSION = "1.6.99";
        private StaticLoggerBinder() {
        throw new UnsupportedOperationException("This code should have never made it into slf4j-api.jar");
        }
        public ILoggerFactory getLoggerFactory() {
        throw new UnsupportedOperationException("This code should never make it into slf4j-api.jar");
        }
        public String getLoggerFactoryClassStr() {
        throw new UnsupportedOperationException("This code should never make it into slf4j-api.jar");
        }
        }
        (StaticLoggerBinder.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `LoggerFactoryBinder.java`

## Method: `public ILoggerFactory getLoggerFactory()`

        <!-- META {"entityType": "Method", "entitySignature": "public ILoggerFactory getLoggerFactory()", "entityFile": "LoggerFactoryBinder.java"} -->Return the instance of ILoggerFactory that
        org.slf4j.LoggerFactory class should bind to.
        @return the instance of ILoggerFactory that
        org.slf4j.LoggerFactory class should bind to.

# File: `IMarkerFactory.java`

## Method: `Marker getMarker(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "Marker getMarker(String name)", "entityFile": "IMarkerFactory.java"} -->Manufacture a Marker instance by name. If the instance has been
        created earlier, return the previously created instance.
        Null name values are not allowed.
        @param name the name of the marker to be created, null value is
        not allowed.
        @return a Marker instance

# File: `LoggerFactoryBinder.java`

## Method: `public String getLoggerFactoryClassStr()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getLoggerFactoryClassStr()", "entityFile": "LoggerFactoryBinder.java"} -->The String form of the ILoggerFactory object that this
        LoggerFactoryBinder instance is intended to return.
        This method allows the developer to intterogate this binder's intention
        which may be different from the ILoggerFactory instance it is able to
        yield in practice. The discrepency should only occur in case of errors.
        @return the class name of the intended ILoggerFactory instance

## Interface: `LoggerFactoryBinder`

        <!-- META {"entityType": "Interface", "entitySignature": "LoggerFactoryBinder", "entityFile": "LoggerFactoryBinder.java"} -->An internal interface which helps the static org.slf4j.LoggerFactory
        class bind with the appropriate ILoggerFactory instance.
        @author Ceki G&uuml;lc&uuml;

# File: `IMarkerFactory.java`

## Method: `boolean exists(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "boolean exists(String name)", "entityFile": "IMarkerFactory.java"} -->Checks if the marker with the name already exists. If name is null, then false
        is returned.
        @param name logger name to check for
        @return true id the marker exists, false otherwise.

# File: `StaticMarkerBinder.java`

## Method: `public static StaticMarkerBinder getSingleton()`

        <!-- META {"entityType": "Method", "entitySignature": "public static StaticMarkerBinder getSingleton()", "entityFile": "StaticMarkerBinder.java"} -->Return the singleton of this class.
        @return the StaticMarkerBinder singleton
        @since 1.7.14

## Method: `public IMarkerFactory getMarkerFactory()`

        <!-- META {"entityType": "Method", "entitySignature": "public IMarkerFactory getMarkerFactory()", "entityFile": "StaticMarkerBinder.java"} -->Currently this method always returns an instance of
        BasicMarkerFactory.

## Method: `public String getMarkerFactoryClassStr()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getMarkerFactoryClassStr()", "entityFile": "StaticMarkerBinder.java"} -->Currently, this method returns the class name of
        BasicMarkerFactory.

# File: `IMarkerFactory.java`

## Method: `boolean detachMarker(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "boolean detachMarker(String name)", "entityFile": "IMarkerFactory.java"} -->Detach an existing marker.
        Note that after a marker is detached, there might still be "dangling" references
        to the detached marker.
        @param name The name of the marker to detach
        @return whether the marker  could be detached or not

# File: `StaticMarkerBinder.java`

## Class: `StaticMarkerBinder`

        <!-- META {"entityType": "Class", "entitySignature": "StaticMarkerBinder", "entityFile": "StaticMarkerBinder.java"} -->The binding of MarkerFactory class with an actual instance of
        IMarkerFactory is performed using information returned by this class.
        This class is meant to provide a *dummy* StaticMarkerBinder to the slf4j-api module.
        Real implementations are found in  each SLF4J binding project, e.g. slf4j-nop,
        slf4j-simple, slf4j-log4j12 etc.
        @author Ceki G&uuml;lc&uuml;

# File: `MessageFormatter.java`

## Class: `MessageFormatter`

        <!-- META {"entityType": "Class", "entitySignature": "MessageFormatter", "entityFile": "MessageFormatter.java"} --><!-- 9e41439c-a242-11e9-b658-333445793454 <=< ACCEPT -->Formats messages according to very simple substitution rules. Substitutions
        can be made 1, 2 or more arguments.
        For example,
        MessageFormatter.format(&quot;Hi {}.&quot;, &quot;there&quot;)
        will return the string "Hi there.".
        The {} pair is called the formatting anchor. It serves to designate
        the location where arguments need to be substituted within the message
        pattern.
        In case your message contains the '{' or the '}' character, you do not have
        to do anything special unless the '}' character immediately follows '{'. For
        example,
        MessageFormatter.format(&quot;Set {1,2,3} is not equal to {}.&quot;, &quot;1,2&quot;);
        will return the string "Set {1,2,3} is not equal to 1,2.".
        If for whatever reason you need to place the string "{}" in the message
        without its formatting anchor meaning, then you need to escape the
        '{' character with '\', that is the backslash character. Only the '{'
        character should be escaped. There is no need to escape the '}' character.
        For example,
        MessageFormatter.format(&quot;Set \\{} is not equal to {}.&quot;, &quot;1,2&quot;);
        will return the string "Set {} is not equal to 1,2.".
        The escaping behavior just described can be overridden by escaping the escape
        character '\'. Calling
        MessageFormatter.format(&quot;File name is C:\\\\{}.&quot;, &quot;file.zip&quot;);
        will return the string "File name is C:\file.zip".
        The formatting conventions are different than those of MessageFormat
        which ships with the Java platform. This is justified by the fact that
        SLF4J's implementation is 10 times faster than that of MessageFormat.
        This local performance difference is both measurable and significant in the
        larger context of the complete logging processing chain.
        See also #format(String, Object),
        #format(String, Object, Object) and
        #arrayFormat(String, Object[]) methods for more details.
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn
        <!-- ACCEPT >=> 9e41439c-a242-11e9-b658-333445793454 -->

# File: `IMarkerFactory.java`

## Method: `Marker getDetachedMarker(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "Marker getDetachedMarker(String name)", "entityFile": "IMarkerFactory.java"} -->Create a marker which is detached (even at birth) from this IMarkerFactory.
        @param name marker name
        @return a dangling marker
        @since 1.5.1

## Interface: `IMarkerFactory`

        <!-- META {"entityType": "Interface", "entitySignature": "IMarkerFactory", "entityFile": "IMarkerFactory.java"} -->Implementations of this interface are used to manufacture Marker
        instances.
        See the section <a href="http://slf4j.org/faq.html#3">Implementing
        the SLF4J API in the FAQ for details on how to make your logging
        system conform to SLF4J.
        @author Ceki G&uuml;lc&uuml;

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.spi;
        import org.slf4j.ILoggerFactory;
        /**
        An internal interface which helps the static org.slf4j.LoggerFactory
        class bind with the appropriate ILoggerFactory instance.
        @author Ceki G&uuml;lc&uuml;
        */
        public interface LoggerFactoryBinder {
        /**
        Return the instance of ILoggerFactory that
        org.slf4j.LoggerFactory class should bind to.
        @return the instance of ILoggerFactory that
        org.slf4j.LoggerFactory class should bind to.
        */
        public ILoggerFactory getLoggerFactory();
        /**
        The String form of the ILoggerFactory object that this
        LoggerFactoryBinder instance is intended to return.
        This method allows the developer to intterogate this binder's intention
        which may be different from the ILoggerFactory instance it is able to
        yield in practice. The discrepency should only occur in case of errors.
        @return the class name of the intended ILoggerFactory instance
        */
        public String getLoggerFactoryClassStr();
        }
        (LoggerFactoryBinder.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.impl;
        import org.slf4j.IMarkerFactory;
        import org.slf4j.MarkerFactory;
        import org.slf4j.helpers.BasicMarkerFactory;
        import org.slf4j.spi.MarkerFactoryBinder;
        /**
        The binding of MarkerFactory class with an actual instance of
        IMarkerFactory is performed using information returned by this class.
        This class is meant to provide a *dummy* StaticMarkerBinder to the slf4j-api module.
        Real implementations are found in  each SLF4J binding project, e.g. slf4j-nop,
        slf4j-simple, slf4j-log4j12 etc.
        @author Ceki G&uuml;lc&uuml;
        */
        public class StaticMarkerBinder implements MarkerFactoryBinder {
        /**
        The unique instance of this class.
        */
        public static final StaticMarkerBinder SINGLETON = new StaticMarkerBinder();
        private StaticMarkerBinder() {
        throw new UnsupportedOperationException("This code should never make it into the jar");
        }
        /**
        Return the singleton of this class.
        @return the StaticMarkerBinder singleton
        @since 1.7.14
        */
        public static StaticMarkerBinder getSingleton() {
        return SINGLETON;
        }
        /**
        Currently this method always returns an instance of
        BasicMarkerFactory.
        */
        public IMarkerFactory getMarkerFactory() {
        throw new UnsupportedOperationException("This code should never make it into the jar");
        }
        /**
        Currently, this method returns the class name of
        BasicMarkerFactory.
        */
        public String getMarkerFactoryClassStr() {
        throw new UnsupportedOperationException("This code should never make it into the jar");
        }
        }
        (StaticMarkerBinder.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `MarkerFactoryBinder.java`

## Method: `public IMarkerFactory getMarkerFactory()`

        <!-- META {"entityType": "Method", "entitySignature": "public IMarkerFactory getMarkerFactory()", "entityFile": "MarkerFactoryBinder.java"} -->Return the instance of IMarkerFactory that
        org.slf4j.MarkerFactory class should bind to.
        @return the instance of IMarkerFactory that
        org.slf4j.MarkerFactory class should bind to.

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.text.MessageFormat;
        import java.util.HashMap;
        import java.util.Map;
        /**
        <!-- 9e41439c-a242-11e9-b658-333445793454 <=< ACCEPT -->Formats messages according to very simple substitution rules. Substitutions
        can be made 1, 2 or more arguments.
        For example,
        MessageFormatter.format(&quot;Hi {}.&quot;, &quot;there&quot;)
        will return the string "Hi there.".
        The {} pair is called the formatting anchor. It serves to designate
        the location where arguments need to be substituted within the message
        pattern.
        In case your message contains the '{' or the '}' character, you do not have
        to do anything special unless the '}' character immediately follows '{'. For
        example,
        MessageFormatter.format(&quot;Set {1,2,3} is not equal to {}.&quot;, &quot;1,2&quot;);
        will return the string "Set {1,2,3} is not equal to 1,2.".
        If for whatever reason you need to place the string "{}" in the message
        without its formatting anchor meaning, then you need to escape the
        '{' character with '\', that is the backslash character. Only the '{'
        character should be escaped. There is no need to escape the '}' character.
        For example,
        MessageFormatter.format(&quot;Set \\{} is not equal to {}.&quot;, &quot;1,2&quot;);
        will return the string "Set {} is not equal to 1,2.".
        The escaping behavior just described can be overridden by escaping the escape
        character '\'. Calling
        MessageFormatter.format(&quot;File name is C:\\\\{}.&quot;, &quot;file.zip&quot;);
        will return the string "File name is C:\file.zip".
        The formatting conventions are different than those of MessageFormat
        which ships with the Java platform. This is justified by the fact that
        SLF4J's implementation is 10 times faster than that of MessageFormat.
        This local performance difference is both measurable and significant in the
        larger context of the complete logging processing chain.
        See also #format(String, Object),
        #format(String, Object, Object) and
        #arrayFormat(String, Object[]) methods for more details.
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn<!-- ACCEPT >=> 9e41439c-a242-11e9-b658-333445793454 -->
        */
        public final class MessageFormatter {
        static final char DELIM_START = '{';
        static final char DELIM_STOP = '}';
        static final String DELIM_STR = "{}";
        private static final char ESCAPE_CHAR = '\\';
        /**
        Performs single argument substitution for the 'messagePattern' passed as
        parameter.
        For example,
        MessageFormatter.format(&quot;Hi {}.&quot;, &quot;there&quot;);
        will return the string "Hi there.".
        @param messagePattern
        The message pattern which will be parsed and formatted
        @param arg
        The argument to be substituted in place of the formatting anchor
        @return The formatted message
        */
        public static final FormattingTuple format(String messagePattern, Object arg) {
        return arrayFormat(messagePattern, new Object[] { arg });
        }
        /**
        Performs a two argument substitution for the 'messagePattern' passed as
        parameter.
        For example,
        MessageFormatter.format(&quot;Hi {}. My name is {}.&quot;, &quot;Alice&quot;, &quot;Bob&quot;);
        will return the string "Hi Alice. My name is Bob.".
        @param messagePattern
        The message pattern which will be parsed and formatted
        @param arg1
        The argument to be substituted in place of the first formatting
        anchor
        @param arg2
        The argument to be substituted in place of the second formatting
        anchor
        @return The formatted message
        */
        public static final FormattingTuple format(final String messagePattern, Object arg1, Object arg2) {
        return arrayFormat(messagePattern, new Object[] { arg1, arg2 });
        }
        static final Throwable getThrowableCandidate(Object[] argArray) {
        if (argArray == null || argArray.length == 0) {
        return null;
        }
        final Object lastEntry = argArray[argArray.length - 1];
        if (lastEntry instanceof Throwable) {
        return (Throwable) lastEntry;
        }
        return null;
        }
        public static final FormattingTuple arrayFormat(final String messagePattern, final Object[] argArray) {
        Throwable throwableCandidate = getThrowableCandidate(argArray);
        Object[] args = argArray;
        if (throwableCandidate != null) {
        args = trimmedCopy(argArray);
        }
        return arrayFormat(messagePattern, args, throwableCandidate);
        }
        private static Object[] trimmedCopy(Object[] argArray) {
        if (argArray == null || argArray.length == 0) {
        throw new IllegalStateException("non-sensical empty or null argument array");
        }
        final int trimemdLen = argArray.length - 1;
        Object[] trimmed = new Object[trimemdLen];
        System.arraycopy(argArray, 0, trimmed, 0, trimemdLen);
        return trimmed;
        }
        public static final FormattingTuple arrayFormat(final String messagePattern, final Object[] argArray, Throwable throwable) {
        if (messagePattern == null) {
        return new FormattingTuple(null, argArray, throwable);
        }
        if (argArray == null) {
        return new FormattingTuple(messagePattern);
        }
        int i = 0;
        int j;
        // use string builder for better multicore performance
        StringBuilder sbuf = new StringBuilder(messagePattern.length() + 50);
        int L;
        for (L = 0; L < argArray.length; L++) {
        j = messagePattern.indexOf(DELIM_STR, i);
        if (j == -1) {
        // no more variables
        if (i == 0) {
        // this is a simple string
        return new FormattingTuple(messagePattern, argArray, throwable);
        } else {
        // add the tail string which contains no variables and return
        // the result.
        sbuf.append(messagePattern, i, messagePattern.length());
        return new FormattingTuple(sbuf.toString(), argArray, throwable);
        }
        } else {
        if (isEscapedDelimeter(messagePattern, j)) {
        if (!isDoubleEscaped(messagePattern, j)) {
        // DELIM_START was escaped, thus should not be incremented
        L--;
        sbuf.append(messagePattern, i, j - 1);
        sbuf.append(DELIM_START);
        i = j + 1;
        } else {
        // The escape character preceding the delimiter start is
        // itself escaped: "abc x:\\{}"
        // we have to consume one backward slash
        sbuf.append(messagePattern, i, j - 1);
        deeplyAppendParameter(sbuf, argArray[L], new HashMap<Object[], Object>());
        i = j + 2;
        }
        } else {
        // normal case
        sbuf.append(messagePattern, i, j);
        deeplyAppendParameter(sbuf, argArray[L], new HashMap<Object[], Object>());
        i = j + 2;
        }
        }
        }
        // append the characters following the last {} pair.
        sbuf.append(messagePattern, i, messagePattern.length());
        return new FormattingTuple(sbuf.toString(), argArray, throwable);
        }
        static final boolean isEscapedDelimeter(String messagePattern, int delimeterStartIndex) {
        if (delimeterStartIndex == 0) {
        return false;
        }
        char potentialEscape = messagePattern.charAt(delimeterStartIndex - 1);
        if (potentialEscape == ESCAPE_CHAR) {
        return true;
        } else {
        return false;
        }
        }
        static final boolean isDoubleEscaped(String messagePattern, int delimeterStartIndex) {
        if (delimeterStartIndex >= 2 && messagePattern.charAt(delimeterStartIndex - 2) == ESCAPE_CHAR) {
        return true;
        } else {
        return false;
        }
        }
        // special treatment of array values was suggested by 'lizongbo'
        private static void deeplyAppendParameter(StringBuilder sbuf, Object o, Map<Object[], Object> seenMap) {
        if (o == null) {
        sbuf.append("null");
        return;
        }
        if (!o.getClass().isArray()) {
        safeObjectAppend(sbuf, o);
        } else {
        // unfortunately cannot be cast to Object[]
        if (o instanceof boolean[]) {
        booleanArrayAppend(sbuf, (boolean[]) o);
        } else if (o instanceof byte[]) {
        byteArrayAppend(sbuf, (byte[]) o);
        } else if (o instanceof char[]) {
        charArrayAppend(sbuf, (char[]) o);
        } else if (o instanceof short[]) {
        shortArrayAppend(sbuf, (short[]) o);
        } else if (o instanceof int[]) {
        intArrayAppend(sbuf, (int[]) o);
        } else if (o instanceof long[]) {
        longArrayAppend(sbuf, (long[]) o);
        } else if (o instanceof float[]) {
        floatArrayAppend(sbuf, (float[]) o);
        } else if (o instanceof double[]) {
        doubleArrayAppend(sbuf, (double[]) o);
        } else {
        objectArrayAppend(sbuf, (Object[]) o, seenMap);
        }
        }
        }
        private static void safeObjectAppend(StringBuilder sbuf, Object o) {
        try {
        String oAsString = o.toString();
        sbuf.append(oAsString);
        } catch (Throwable t) {
        Util.report("SLF4J: Failed toString() invocation on an object of type [" + o.getClass().getName() + "]", t);
        sbuf.append("[FAILED toString()]");
        }
        }
        private static void objectArrayAppend(StringBuilder sbuf, Object[] a, Map<Object[], Object> seenMap) {
        sbuf.append('[');
        if (!seenMap.containsKey(a)) {
        seenMap.put(a, null);
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        deeplyAppendParameter(sbuf, a[i], seenMap);
        if (i != len - 1)
        sbuf.append(", ");
        }
        // allow repeats in siblings
        seenMap.remove(a);
        } else {
        sbuf.append("...");
        }
        sbuf.append(']');
        }
        private static void booleanArrayAppend(StringBuilder sbuf, boolean[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void byteArrayAppend(StringBuilder sbuf, byte[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void charArrayAppend(StringBuilder sbuf, char[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void shortArrayAppend(StringBuilder sbuf, short[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void intArrayAppend(StringBuilder sbuf, int[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void longArrayAppend(StringBuilder sbuf, long[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void floatArrayAppend(StringBuilder sbuf, float[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        private static void doubleArrayAppend(StringBuilder sbuf, double[] a) {
        sbuf.append('[');
        final int len = a.length;
        for (int i = 0; i < len; i++) {
        sbuf.append(a[i]);
        if (i != len - 1)
        sbuf.append(", ");
        }
        sbuf.append(']');
        }
        }
        (MessageFormatter.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        /**
        Implementations of this interface are used to manufacture Marker
        instances.
        See the section <a href="http://slf4j.org/faq.html#3">Implementing
        the SLF4J API in the FAQ for details on how to make your logging
        system conform to SLF4J.
        @author Ceki G&uuml;lc&uuml;
        */
        public interface IMarkerFactory {
        /**
        Manufacture a Marker instance by name. If the instance has been
        created earlier, return the previously created instance.
        Null name values are not allowed.
        @param name the name of the marker to be created, null value is
        not allowed.
        @return a Marker instance
        */
        Marker getMarker(String name);
        /**
        Checks if the marker with the name already exists. If name is null, then false
        is returned.
        @param name logger name to check for
        @return true id the marker exists, false otherwise.
        */
        boolean exists(String name);
        /**
        Detach an existing marker.
        Note that after a marker is detached, there might still be "dangling" references
        to the detached marker.
        @param name The name of the marker to detach
        @return whether the marker  could be detached or not
        */
        boolean detachMarker(String name);
        /**
        Create a marker which is detached (even at birth) from this IMarkerFactory.
        @param name marker name
        @return a dangling marker
        @since 1.5.1
        */
        Marker getDetachedMarker(String name);
        }
        (IMarkerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        <!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `MarkerFactoryBinder.java`

## Method: `public String getMarkerFactoryClassStr()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getMarkerFactoryClassStr()", "entityFile": "MarkerFactoryBinder.java"} -->The String form of the IMarkerFactory object that this
        MarkerFactoryBinder instance is intended to return.
        This method allows the developer to intterogate this binder's intention
        which may be different from the IMarkerFactory instance it is able to
        return. Such a discrepency should only occur in case of errors.
        @return the class name of the intended IMarkerFactory instance

## Interface: `MarkerFactoryBinder`

        <!-- META {"entityType": "Interface", "entitySignature": "MarkerFactoryBinder", "entityFile": "MarkerFactoryBinder.java"} -->An internal interface which helps the static org.slf4j.MarkerFactory
        class bind with the appropriate IMarkerFactory instance.
        @author Ceki G&uuml;lc&uuml;

# File: `StaticMDCBinder.java`

## Method: `public static final StaticMDCBinder getSingleton()`

        <!-- META {"entityType": "Method", "entitySignature": "public static final StaticMDCBinder getSingleton()", "entityFile": "StaticMDCBinder.java"} -->Return the singleton of this class.
        @return the StaticMDCBinder singleton
        @since 1.7.14

# File: `SubstituteLoggerFactory.java`

## Class: `SubstituteLoggerFactory`

        <!-- META {"entityType": "Class", "entitySignature": "SubstituteLoggerFactory", "entityFile": "SubstituteLoggerFactory.java"} -->SubstituteLoggerFactory manages instances of SubstituteLogger.
        @author Ceki G&uuml;lc&uuml;
        @author Chetan Mehrotra

# File: `StaticMDCBinder.java`

## Method: `public MDCAdapter getMDCA()`

        <!-- META {"entityType": "Method", "entitySignature": "public MDCAdapter getMDCA()", "entityFile": "StaticMDCBinder.java"} -->Currently this method always returns an instance of
        StaticMDCBinder.

## Class: `StaticMDCBinder`

        <!-- META {"entityType": "Class", "entitySignature": "StaticMDCBinder", "entityFile": "StaticMDCBinder.java"} -->This class is only a stub. Real implementations are found in
        each SLF4J binding project, e.g. slf4j-nop, slf4j-log4j12 etc.
        @author Ceki G&uuml;lc&uuml;

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.spi;
        import org.slf4j.IMarkerFactory;
        /**
        An internal interface which helps the static org.slf4j.MarkerFactory
        class bind with the appropriate IMarkerFactory instance.
        @author Ceki G&uuml;lc&uuml;
        */
        public interface MarkerFactoryBinder {
        /**
        Return the instance of IMarkerFactory that
        org.slf4j.MarkerFactory class should bind to.
        @return the instance of IMarkerFactory that
        org.slf4j.MarkerFactory class should bind to.
        */
        public IMarkerFactory getMarkerFactory();
        /**
        The String form of the IMarkerFactory object that this
        MarkerFactoryBinder instance is intended to return.
        This method allows the developer to intterogate this binder's intention
        which may be different from the IMarkerFactory instance it is able to
        return. Such a discrepency should only occur in case of errors.
        @return the class name of the intended IMarkerFactory instance
        */
        public String getMarkerFactoryClassStr();
        }
        (MarkerFactoryBinder.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.impl;
        import org.slf4j.spi.MDCAdapter;
        /**
        This class is only a stub. Real implementations are found in
        each SLF4J binding project, e.g. slf4j-nop, slf4j-log4j12 etc.
        @author Ceki G&uuml;lc&uuml;
        */
        public class StaticMDCBinder {
        /**
        The unique instance of this class.
        */
        public static final StaticMDCBinder SINGLETON = new StaticMDCBinder();
        private StaticMDCBinder() {
        throw new UnsupportedOperationException("This code should never make it into the jar");
        }
        /**
        Return the singleton of this class.
        @return the StaticMDCBinder singleton
        @since 1.7.14
        */
        public static final StaticMDCBinder getSingleton() {
        return SINGLETON;
        }
        /**
        Currently this method always returns an instance of
        StaticMDCBinder.
        */
        public MDCAdapter getMDCA() {
        throw new UnsupportedOperationException("This code should never make it into the jar");
        }
        public String getMDCAdapterClassStr() {
        throw new UnsupportedOperationException("This code should never make it into the jar");
        }
        }
        (StaticMDCBinder.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.util.ArrayList;
        import java.util.List;
        import java.util.concurrent.ConcurrentHashMap;
        import java.util.concurrent.ConcurrentMap;
        import java.util.concurrent.LinkedBlockingQueue;
        import org.slf4j.ILoggerFactory;
        import org.slf4j.Logger;
        import org.slf4j.event.SubstituteLoggingEvent;
        /**
        SubstituteLoggerFactory manages instances of SubstituteLogger.
        @author Ceki G&uuml;lc&uuml;
        @author Chetan Mehrotra
        */
        public class SubstituteLoggerFactory implements ILoggerFactory {
        final ConcurrentMap<String, SubstituteLogger> loggers = new ConcurrentHashMap<String, SubstituteLogger>();
        final LinkedBlockingQueue<SubstituteLoggingEvent> eventQueue = new LinkedBlockingQueue<SubstituteLoggingEvent>();
        public Logger getLogger(String name) {
        SubstituteLogger logger = loggers.get(name);
        if (logger == null) {
        logger = new SubstituteLogger(name, eventQueue);
        SubstituteLogger oldLogger = loggers.putIfAbsent(name, logger);
        if (oldLogger != null)
        logger = oldLogger;
        }
        return logger;
        }
        public List<String> getLoggerNames() {
        return new ArrayList<String>(loggers.keySet());
        }
        public List<SubstituteLogger> getLoggers() {
        return new ArrayList<SubstituteLogger>(loggers.values());
        }
        public LinkedBlockingQueue<SubstituteLoggingEvent> getEventQueue() {
        return eventQueue;
        }
        public void clear() {
        loggers.clear();
        eventQueue.clear();
        }
        }
        (SubstituteLoggerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `NamedLoggerBase.java`

## Method: `protected Object readResolve() throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "protected Object readResolve() throws ObjectStreamException", "entityFile": "NamedLoggerBase.java"} -->Replace this instance with a homonymous (same name) logger returned
        by LoggerFactory. Note that this method is only called during
        deserialization.
        This approach will work well if the desired ILoggerFactory is the one
        references by LoggerFactory. However, if the user manages its logger hierarchy
        through a different (non-static) mechanism, e.g. dependency injection, then
        this approach would be mostly counterproductive.
        @return logger with same name as returned by LoggerFactory
        @throws ObjectStreamException

## Class: `NamedLoggerBase`

        <!-- META {"entityType": "Class", "entitySignature": "NamedLoggerBase", "entityFile": "NamedLoggerBase.java"} -->Serves as base class for named logger implementation. More significantly, this
        class establishes deserialization behavior. See @see #readResolve.
        @author Ceki Gulcu
        @since 1.5.3

# File: `MDCAdapter.java`

## Method: `public void put(String key, String val)`

        <!-- META {"entityType": "Method", "entitySignature": "public void put(String key, String val)", "entityFile": "MDCAdapter.java"} --><!-- fa1791e4-1793-11ea-a362-333445793454 <=< ACCEPT -->Put a context value (the val parameter) as identified with
        the key parameter into the current thread's context map.
        The key parameter cannot be null. The code>val parameter
        can be null only if the underlying implementation supports it.
        If the current thread does not have a context map it is created as a side
        effect of this call.<!-- ACCEPT >=> fa1791e4-1793-11ea-a362-333445793454 -->

## Method: `public String get(String key)`

        <!-- META {"entityType": "Method", "entitySignature": "public String get(String key)", "entityFile": "MDCAdapter.java"} -->Get the context identified by the key parameter.
        The key parameter cannot be null.
        @return the string value identified by the key parameter.

## Method: `public void remove(String key)`

        <!-- META {"entityType": "Method", "entitySignature": "public void remove(String key)", "entityFile": "MDCAdapter.java"} -->Remove the the context identified by the key parameter.
        The key parameter cannot be null.
        This method does nothing if there is no previous value
        associated with key.

## Method: `public Map<String, String> getCopyOfContextMap()`

        <!-- META {"entityType": "Method", "entitySignature": "public Map<String, String> getCopyOfContextMap()", "entityFile": "MDCAdapter.java"} -->Return a copy of the current thread's context map, with keys and
        values of type String. Returned value may be null.
        @return A copy of the current thread's context map. May be null.
        @since 1.5.1

# File: `Util.java`

## Class: `ClassContextSecurityManager`

        <!-- META {"entityType": "Class", "entitySignature": "ClassContextSecurityManager", "entityFile": "Util.java"} -->In order to call SecurityManager#getClassContext(), which is a
        protected method, we add this wrapper which allows the method to be visible
        inside this package.

## Method: `public static Class<?> getCallingClass()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class<?> getCallingClass()", "entityFile": "Util.java"} -->Returns the name of the class which called the invoking method.
        @return the name of the class which called the invoking method.

## Class: `Util`

        <!-- META {"entityType": "Class", "entitySignature": "Util", "entityFile": "Util.java"} -->An internal utility class.
        @author Alexander Dorokhine
        @author Ceki G&uuml;lc&uuml;

# File: `MDCAdapter.java`

## Method: `public void setContextMap(Map<String, String> contextMap)`

        <!-- META {"entityType": "Method", "entitySignature": "public void setContextMap(Map<String, String> contextMap)", "entityFile": "MDCAdapter.java"} -->Set the current thread's context map by first clearing any existing
        map and then copying the map passed as parameter. The context map
        parameter must only contain keys and values of type String.
        @param contextMap must contain only keys and values of type String
        @since 1.5.1

# File: `Logger.java`

## Field: `ROOT_LOGGER_NAME`

        <!-- META {"entityType": "Field", "entitySignature": "ROOT_LOGGER_NAME", "entityFile": "Logger.java"} -->Case insensitive String constant used to retrieve the name of the root logger.
        @since 1.3

## Method: `public String getName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getName()", "entityFile": "Logger.java"} -->Return the name of this Logger instance.
        @return name of this logger instance

## Method: `public boolean isTraceEnabled()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isTraceEnabled()", "entityFile": "Logger.java"} -->Is the logger instance enabled for the TRACE level?
        @return True if this Logger is enabled for the TRACE level,
        false otherwise.
        @since 1.4

## Method: `public void trace(String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(String msg)", "entityFile": "Logger.java"} -->Log a message at the TRACE level.
        @param msg the message string to be logged
        @since 1.4

## Method: `public void trace(String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(String format, Object arg)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the TRACE level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the TRACE level.
        @param format the format string
        @param arg    the argument
        @since 1.4<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        /**
        An internal utility class.
        @author Alexander Dorokhine
        @author Ceki G&uuml;lc&uuml;
        */
        public final class Util {
        private Util() {
        }
        public static String safeGetSystemProperty(String key) {
        if (key == null)
        throw new IllegalArgumentException("null input");
        String result = null;
        try {
        result = System.getProperty(key);
        } catch (java.lang.SecurityException sm) {
        // ignore
        ;
        }
        return result;
        }
        public static boolean safeGetBooleanSystemProperty(String key) {
        String value = safeGetSystemProperty(key);
        if (value == null)
        return false;
        else
        return value.equalsIgnoreCase("true");
        }
        /**
        In order to call SecurityManager#getClassContext(), which is a
        protected method, we add this wrapper which allows the method to be visible
        inside this package.
        */
        private static final class ClassContextSecurityManager extends SecurityManager {
        protected Class<?>[] getClassContext() {
        return super.getClassContext();
        }
        }
        private static ClassContextSecurityManager SECURITY_MANAGER;
        private static boolean SECURITY_MANAGER_CREATION_ALREADY_ATTEMPTED = false;
        private static ClassContextSecurityManager getSecurityManager() {
        if (SECURITY_MANAGER != null)
        return SECURITY_MANAGER;
        else if (SECURITY_MANAGER_CREATION_ALREADY_ATTEMPTED)
        return null;
        else {
        SECURITY_MANAGER = safeCreateSecurityManager();
        SECURITY_MANAGER_CREATION_ALREADY_ATTEMPTED = true;
        return SECURITY_MANAGER;
        }
        }
        private static ClassContextSecurityManager safeCreateSecurityManager() {
        try {
        return new ClassContextSecurityManager();
        } catch (java.lang.SecurityException sm) {
        return null;
        }
        }
        /**
        Returns the name of the class which called the invoking method.
        @return the name of the class which called the invoking method.
        */
        public static Class<?> getCallingClass() {
        # Class ContextSecurityManager securityManager = getSecurityManager();
        if (securityManager == null)
        return null;
        # Class <?>[] trace = securityManager.getClassContext();
        String thisClassName = Util.class.getName();
        // Advance until Util is found
        int i;
        for (i = 0; i < trace.length; i++) {
        if (thisClassName.equals(trace[i].getName()))
        break;
        }
        // trace[i] = Util; trace[i+1] = caller; trace[i+2] = caller's caller
        if (i >= trace.length || i + 2 >= trace.length) {
        throw new IllegalStateException("Failed to find org.slf4j.helpers.Util or its caller in the stack; " + "this should not happen");
        }
        return trace[i + 2];
        }
        public static final void report(String msg, Throwable t) {
        System.err.println(msg);
        System.err.println("Reported exception:");
        t.printStackTrace();
        }
        public static final void report(String msg) {
        System.err.println("SLF4J: " + msg);
        }
        }
        (Util.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void trace(String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} -->Log a message at the TRACE level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the TRACE level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        @since 1.4

# File: `MDCAdapter.java`

## Interface: `MDCAdapter`

        <!-- META {"entityType": "Interface", "entitySignature": "MDCAdapter", "entityFile": "MDCAdapter.java"} -->This interface abstracts the service offered by various MDC
        implementations.
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.io.ObjectStreamException;
        import java.io.Serializable;
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        /**
        Serves as base class for named logger implementation. More significantly, this
        class establishes deserialization behavior. See @see #readResolve.
        @author Ceki Gulcu
        @since 1.5.3
        */
        abstract class NamedLoggerBase implements Logger, Serializable {
        private static final long serialVersionUID = 7535258609338176893L;
        protected String name;
        public String getName() {
        return name;
        }
        /**
        Replace this instance with a homonymous (same name) logger returned
        by LoggerFactory. Note that this method is only called during
        deserialization.
        This approach will work well if the desired ILoggerFactory is the one
        references by LoggerFactory. However, if the user manages its logger hierarchy
        through a different (non-static) mechanism, e.g. dependency injection, then
        this approach would be mostly counterproductive.
        @return logger with same name as returned by LoggerFactory
        @throws ObjectStreamException
        */
        protected Object readResolve() throws ObjectStreamException {
        // NOPLogger
        return LoggerFactory.getLogger(getName());
        }
        }
        (NamedLoggerBase.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void trace(String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- ae8c9e26-a243-11e9-9f89-333445793454 <=< ACCEPT -->Log a message at the TRACE level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the TRACE level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for TRACE. The variants taking #trace(String, Object) one and
        #trace(String, Object, Object) two arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments
        @since 1.4<!-- ACCEPT >=> ae8c9e26-a243-11e9-9f89-333445793454 -->

## Method: `public void trace(String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(String msg, Throwable t)", "entityFile": "Logger.java"} -->Log an exception (throwable) at the TRACE level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        @since 1.4

## Method: `public boolean isTraceEnabled(Marker marker)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isTraceEnabled(Marker marker)", "entityFile": "Logger.java"} --><!-- 6aee5d7e-a244-11e9-8feb-333445793454 <=< ACCEPT -->Similar to #isTraceEnabled() method except that the
        marker data is also taken into account.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the TRACE level,
        false otherwise.
        @since 1.4<!-- ACCEPT >=> 6aee5d7e-a244-11e9-8feb-333445793454 -->

## Method: `public void trace(Marker marker, String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(Marker marker, String msg)", "entityFile": "Logger.java"} --><!-- e5db5ac6-1796-11ea-84d9-333445793454 <=< ACCEPT -->Log a message with the specific Marker at the TRACE level.
        @param marker the marker data specific to this log statement
        @param msg    the message string to be logged
        @since 1.4<!-- ACCEPT >=> e5db5ac6-1796-11ea-84d9-333445793454 -->

# File: `MarkerFactory.java`

## Method: `private static IMarkerFactory bwCompatibleGetMarkerFactoryFromBinder() throws NoClassDefFoundError`

        <!-- META {"entityType": "Method", "entitySignature": "private static IMarkerFactory bwCompatibleGetMarkerFactoryFromBinder() throws NoClassDefFoundError", "entityFile": "MarkerFactory.java"} -->As of SLF4J version 1.7.14, StaticMarkerBinder classes shipping in various bindings
        come with a getSingleton() method. Previously only a public field called SINGLETON
        was available.
        @return IMarkerFactory
        @throws NoClassDefFoundError in case no binding is available
        @since 1.7.14

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.spi;
        import java.util.Map;
        /**
        This interface abstracts the service offered by various MDC
        implementations.
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1
        */
        public interface MDCAdapter {
        /**
        Put a context value (the val parameter) as identified with
        the key parameter into the current thread's context map.
        The key parameter cannot be null. The code>val parameter
        can be null only if the underlying implementation supports it.
        If the current thread does not have a context map it is created as a side
        effect of this call.
        */
        public void put(String key, String val);
        /**
        Get the context identified by the key parameter.
        The key parameter cannot be null.
        @return the string value identified by the key parameter.
        */
        public String get(String key);
        /**
        Remove the the context identified by the key parameter.
        The key parameter cannot be null.
        This method does nothing if there is no previous value
        associated with key.
        */
        public void remove(String key);
        /**
        Clear all entries in the MDC.
        */
        public void clear();
        /**
        Return a copy of the current thread's context map, with keys and
        values of type String. Returned value may be null.
        @return A copy of the current thread's context map. May be null.
        @since 1.5.1
        */
        public Map<String, String> getCopyOfContextMap();
        /**
        Set the current thread's context map by first clearing any existing
        map and then copying the map passed as parameter. The context map
        parameter must only contain keys and values of type String.
        @param contextMap must contain only keys and values of type String
        @since 1.5.1
        */
        public void setContextMap(Map<String, String> contextMap);
        }
        (MDCAdapter.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void trace(Marker marker, String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(Marker marker, String format, Object arg)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #trace(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        @since 1.4<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `FormattingTuple.java`

## Class: `FormattingTuple`

        <!-- META {"entityType": "Class", "entitySignature": "FormattingTuple", "entityFile": "FormattingTuple.java"} -->Holds the results of formatting done by MessageFormatter.
        @author Joern Huxhorn

# File: `Logger.java`

## Method: `public void trace(Marker marker, String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(Marker marker, String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #trace(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        @since 1.4<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void trace(Marker marker, String format, Object... argArray)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(Marker marker, String format, Object... argArray)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #trace(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker   the marker data specific to this log statement
        @param format   the format string
        @param argArray an array of arguments
        @since 1.4<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `MarkerFactory.java`

## Method: `public static Marker getMarker(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Marker getMarker(String name)", "entityFile": "MarkerFactory.java"} -->Return a Marker instance as specified by the name parameter using the
        previously bound IMarkerFactoryinstance.
        @param name
        The name of the Marker object to return.
        @return marker

# File: `Logger.java`

## Method: `public void trace(Marker marker, String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void trace(Marker marker, String msg, Throwable t)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #trace(String, Throwable) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        @since 1.4<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public boolean isDebugEnabled()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isDebugEnabled()", "entityFile": "Logger.java"} -->Is the logger instance enabled for the DEBUG level?
        @return True if this Logger is enabled for the DEBUG level,
        false otherwise.

## Method: `public void debug(String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(String msg)", "entityFile": "Logger.java"} -->Log a message at the DEBUG level.
        @param msg the message string to be logged

# File: `MarkerFactory.java`

## Method: `public static Marker getDetachedMarker(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Marker getDetachedMarker(String name)", "entityFile": "MarkerFactory.java"} -->Create a marker which is detached (even at birth) from the MarkerFactory.
        @param name the name of the marker
        @return a dangling marker
        @since 1.5.1

## Method: `public static IMarkerFactory getIMarkerFactory()`

        <!-- META {"entityType": "Method", "entitySignature": "public static IMarkerFactory getIMarkerFactory()", "entityFile": "MarkerFactory.java"} -->Return the IMarkerFactoryinstance in use.
        The IMarkerFactory instance is usually bound with this class at
        compile time.
        @return the IMarkerFactory instance in use

# File: `Logger.java`

## Method: `public void debug(String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(String format, Object arg)", "entityFile": "Logger.java"} -->Log a message at the DEBUG level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the DEBUG level.
        @param format the format string
        @param arg    the argument

# File: `MarkerFactory.java`

## Class: `MarkerFactory`

        <!-- META {"entityType": "Class", "entitySignature": "MarkerFactory", "entityFile": "MarkerFactory.java"} -->MarkerFactory is a utility class producing Marker instances as
        appropriate for the logging system currently in use.
        This class is essentially implemented as a wrapper around an
        IMarkerFactory instance bound at compile time.
        Please note that all methods in this class are static.
        @author Ceki G&uuml;lc&uuml;

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        /**
        Holds the results of formatting done by MessageFormatter.
        @author Joern Huxhorn
        */
        public class FormattingTuple {
        public static FormattingTuple NULL = new FormattingTuple(null);
        private String message;
        private Throwable throwable;
        private Object[] argArray;
        public FormattingTuple(String message) {
        this(message, null, null);
        }
        public FormattingTuple(String message, Object[] argArray, Throwable throwable) {
        this.message = message;
        this.throwable = throwable;
        this.argArray = argArray;
        }
        public String getMessage() {
        return message;
        }
        public Object[] getArgArray() {
        return argArray;
        }
        public Throwable getThrowable() {
        return throwable;
        }
        }
        (FormattingTuple.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void debug(String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the DEBUG level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the DEBUG level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        import org.slf4j.helpers.BasicMarkerFactory;
        import org.slf4j.helpers.Util;
        import org.slf4j.impl.StaticMarkerBinder;
        /**
        MarkerFactory is a utility class producing Marker instances as
        appropriate for the logging system currently in use.
        This class is essentially implemented as a wrapper around an
        IMarkerFactory instance bound at compile time.
        Please note that all methods in this class are static.
        @author Ceki G&uuml;lc&uuml;
        */
        public class MarkerFactory {
        static IMarkerFactory MARKER_FACTORY;
        private MarkerFactory() {
        }
        /**
        As of SLF4J version 1.7.14, StaticMarkerBinder classes shipping in various bindings
        come with a getSingleton() method. Previously only a public field called SINGLETON
        was available.
        @return IMarkerFactory
        @throws NoClassDefFoundError in case no binding is available
        @since 1.7.14
        */
        private static IMarkerFactory bwCompatibleGetMarkerFactoryFromBinder() throws NoClassDefFoundError {
        try {
        return StaticMarkerBinder.getSingleton().getMarkerFactory();
        } catch (NoSuchMethodError nsme) {
        // binding is probably a version of SLF4J older than 1.7.14
        return StaticMarkerBinder.SINGLETON.getMarkerFactory();
        }
        }
        // this is where the binding happens
        static {
        try {
        MARKER_FACTORY = bwCompatibleGetMarkerFactoryFromBinder();
        } catch (NoClassDefFoundError e) {
        MARKER_FACTORY = new BasicMarkerFactory();
        } catch (Exception e) {
        // we should never get here
        Util.report("Unexpected failure while binding MarkerFactory", e);
        }
        }
        /**
        Return a Marker instance as specified by the name parameter using the
        previously bound IMarkerFactoryinstance.
        @param name
        The name of the Marker object to return.
        @return marker
        */
        public static Marker getMarker(String name) {
        return MARKER_FACTORY.getMarker(name);
        }
        /**
        Create a marker which is detached (even at birth) from the MarkerFactory.
        @param name the name of the marker
        @return a dangling marker
        @since 1.5.1
        */
        public static Marker getDetachedMarker(String name) {
        return MARKER_FACTORY.getDetachedMarker(name);
        }
        /**
        Return the IMarkerFactoryinstance in use.
        The IMarkerFactory instance is usually bound with this class at
        compile time.
        @return the IMarkerFactory instance in use
        */
        public static IMarkerFactory getIMarkerFactory() {
        return MARKER_FACTORY;
        }
        }
        (MarkerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void debug(String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- ae8c9e26-a243-11e9-9f89-333445793454 <=< ACCEPT -->Log a message at the DEBUG level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the DEBUG level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for DEBUG. The variants taking
        #debug(String, Object) one and #debug(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> ae8c9e26-a243-11e9-9f89-333445793454 -->

## Method: `public void debug(String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(String msg, Throwable t)", "entityFile": "Logger.java"} -->Log an exception (throwable) at the DEBUG level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

## Method: `public boolean isDebugEnabled(Marker marker)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isDebugEnabled(Marker marker)", "entityFile": "Logger.java"} --><!-- 6aee5d7e-a244-11e9-8feb-333445793454 <=< ACCEPT -->Similar to #isDebugEnabled() method except that the
        marker data is also taken into account.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the DEBUG level,
        false otherwise.<!-- ACCEPT >=> 6aee5d7e-a244-11e9-8feb-333445793454 -->

# File: `MarkerIgnoringBase.java`

## Class: `MarkerIgnoringBase`

        <!-- META {"entityType": "Class", "entitySignature": "MarkerIgnoringBase", "entityFile": "MarkerIgnoringBase.java"} -->This class serves as base for adapters or native implementations of logging systems
        lacking Marker support. In this implementation, methods taking marker data
        simply invoke the corresponding method without the Marker argument, discarding
        any marker data passed as argument.
        @author Ceki Gulcu

# File: `Logger.java`

## Method: `public void debug(Marker marker, String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(Marker marker, String msg)", "entityFile": "Logger.java"} --><!-- e5db5ac6-1796-11ea-84d9-333445793454 <=< ACCEPT -->Log a message with the specific Marker at the DEBUG level.
        @param marker the marker data specific to this log statement
        @param msg    the message string to be logged<!-- ACCEPT >=> e5db5ac6-1796-11ea-84d9-333445793454 -->

## Method: `public void debug(Marker marker, String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(Marker marker, String format, Object arg)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #debug(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void debug(Marker marker, String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(Marker marker, String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #debug(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `MDC.java`

## Method: `private static MDCAdapter bwCompatibleGetMDCAdapterFromBinder() throws NoClassDefFoundError`

        <!-- META {"entityType": "Method", "entitySignature": "private static MDCAdapter bwCompatibleGetMDCAdapterFromBinder() throws NoClassDefFoundError", "entityFile": "MDC.java"} -->As of SLF4J version 1.7.14, StaticMDCBinder classes shipping in various bindings
        come with a getSingleton() method. Previously only a public field called SINGLETON
        was available.
        @return MDCAdapter
        @throws NoClassDefFoundError in case no binding is available
        @since 1.7.14

## Method: `public static void put(String key, String val) throws IllegalArgumentException`

        <!-- META {"entityType": "Method", "entitySignature": "public static void put(String key, String val) throws IllegalArgumentException", "entityFile": "MDC.java"} --><!-- 1ca155de-1794-11ea-b0d3-333445793454 <=< ACCEPT -->Put a diagnostic context value (the val parameter) as identified with the
        key parameter into the current thread's diagnostic context map. The
        key parameter cannot be null. The val parameter
        can be null only if the underlying implementation supports it.
        This method delegates all work to the MDC of the underlying logging system.
        @param key non-null key
        @param val value to put in the map
        @throws IllegalArgumentException
        in case the "key" parameter is null<!-- ACCEPT >=> 1ca155de-1794-11ea-b0d3-333445793454 -->

## Method: `public static MDCCloseable putCloseable(String key, String val) throws IllegalArgumentException`

        <!-- META {"entityType": "Method", "entitySignature": "public static MDCCloseable putCloseable(String key, String val) throws IllegalArgumentException", "entityFile": "MDC.java"} --><!-- 1ca155de-1794-11ea-b0d3-333445793454 <=< ACCEPT -->Put a diagnostic context value (the val parameter) as identified with the
        key parameter into the current thread's diagnostic context map. The
        key parameter cannot be null. The val parameter
        can be null only if the underlying implementation supports it.
        This method delegates all work to the MDC of the underlying logging system.
        This method return a Closeable object who can remove key when
        close is called.
        Useful with Java 7 for example :
        try(MDC.MDCCloseable closeable = MDC.putCloseable(key, value)) {
        ....
        }
        @param key non-null key
        @param val value to put in the map
        @return a Closeable who can remove key when close
        is called.
        @throws IllegalArgumentException
        in case the "key" parameter is null<!-- ACCEPT >=> 1ca155de-1794-11ea-b0d3-333445793454 -->

# File: `BasicMarker.java`

## Class: `BasicMarker`

        <!-- META {"entityType": "Class", "entitySignature": "BasicMarker", "entityFile": "BasicMarker.java"} -->A simple implementation of the Marker interface.
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn

# File: `MDC.java`

## Method: `public static String get(String key) throws IllegalArgumentException`

        <!-- META {"entityType": "Method", "entitySignature": "public static String get(String key) throws IllegalArgumentException", "entityFile": "MDC.java"} -->Get the diagnostic context identified by the key parameter. The
        key parameter cannot be null.
        This method delegates all work to the MDC of the underlying logging system.
        @param key
        @return the string value identified by the key parameter.
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `public static void remove(String key) throws IllegalArgumentException`

        <!-- META {"entityType": "Method", "entitySignature": "public static void remove(String key) throws IllegalArgumentException", "entityFile": "MDC.java"} -->Remove the diagnostic context identified by the key parameter using
        the underlying system's MDC implementation. The key parameter
        cannot be null. This method does nothing if there is no previous value
        associated with key.
        @param key
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `public static void clear()`

        <!-- META {"entityType": "Method", "entitySignature": "public static void clear()", "entityFile": "MDC.java"} -->Clear all entries in the MDC of the underlying implementation.

# File: `Logger.java`

## Method: `public void debug(Marker marker, String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(Marker marker, String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #debug(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import org.slf4j.Logger;
        import org.slf4j.Marker;
        /**
        This class serves as base for adapters or native implementations of logging systems
        lacking Marker support. In this implementation, methods taking marker data
        simply invoke the corresponding method without the Marker argument, discarding
        any marker data passed as argument.
        @author Ceki Gulcu
        */
        public abstract class MarkerIgnoringBase extends NamedLoggerBase implements Logger {
        private static final long serialVersionUID = 9044267456635152283L;
        public boolean isTraceEnabled(Marker marker) {
        return isTraceEnabled();
        }
        public void trace(Marker marker, String msg) {
        trace(msg);
        }
        public void trace(Marker marker, String format, Object arg) {
        trace(format, arg);
        }
        public void trace(Marker marker, String format, Object arg1, Object arg2) {
        trace(format, arg1, arg2);
        }
        public void trace(Marker marker, String format, Object... arguments) {
        trace(format, arguments);
        }
        public void trace(Marker marker, String msg, Throwable t) {
        trace(msg, t);
        }
        public boolean isDebugEnabled(Marker marker) {
        return isDebugEnabled();
        }
        public void debug(Marker marker, String msg) {
        debug(msg);
        }
        public void debug(Marker marker, String format, Object arg) {
        debug(format, arg);
        }
        public void debug(Marker marker, String format, Object arg1, Object arg2) {
        debug(format, arg1, arg2);
        }
        public void debug(Marker marker, String format, Object... arguments) {
        debug(format, arguments);
        }
        public void debug(Marker marker, String msg, Throwable t) {
        debug(msg, t);
        }
        public boolean isInfoEnabled(Marker marker) {
        return isInfoEnabled();
        }
        public void info(Marker marker, String msg) {
        info(msg);
        }
        public void info(Marker marker, String format, Object arg) {
        info(format, arg);
        }
        public void info(Marker marker, String format, Object arg1, Object arg2) {
        info(format, arg1, arg2);
        }
        public void info(Marker marker, String format, Object... arguments) {
        info(format, arguments);
        }
        public void info(Marker marker, String msg, Throwable t) {
        info(msg, t);
        }
        public boolean isWarnEnabled(Marker marker) {
        return isWarnEnabled();
        }
        public void warn(Marker marker, String msg) {
        warn(msg);
        }
        public void warn(Marker marker, String format, Object arg) {
        warn(format, arg);
        }
        public void warn(Marker marker, String format, Object arg1, Object arg2) {
        warn(format, arg1, arg2);
        }
        public void warn(Marker marker, String format, Object... arguments) {
        warn(format, arguments);
        }
        public void warn(Marker marker, String msg, Throwable t) {
        warn(msg, t);
        }
        public boolean isErrorEnabled(Marker marker) {
        return isErrorEnabled();
        }
        public void error(Marker marker, String msg) {
        error(msg);
        }
        public void error(Marker marker, String format, Object arg) {
        error(format, arg);
        }
        public void error(Marker marker, String format, Object arg1, Object arg2) {
        error(format, arg1, arg2);
        }
        public void error(Marker marker, String format, Object... arguments) {
        error(format, arguments);
        }
        public void error(Marker marker, String msg, Throwable t) {
        error(msg, t);
        }
        public String toString() {
        return this.getClass().getName() + "(" + getName() + ")";
        }
        }
        (MarkerIgnoringBase.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void debug(Marker marker, String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void debug(Marker marker, String msg, Throwable t)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #debug(String, Throwable) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public boolean isInfoEnabled()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isInfoEnabled()", "entityFile": "Logger.java"} -->Is the logger instance enabled for the INFO level?
        @return True if this Logger is enabled for the INFO level,
        false otherwise.

# File: `NOPMDCAdapter.java`

## Class: `NOPMDCAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "NOPMDCAdapter", "entityFile": "NOPMDCAdapter.java"} -->This adapter is an empty implementation of the MDCAdapter interface.
        It is used for all logging systems which do not support mapped
        diagnostic contexts such as JDK14, simple and NOP.
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1

# File: `MDC.java`

## Method: `public static Map<String, String> getCopyOfContextMap()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Map<String, String> getCopyOfContextMap()", "entityFile": "MDC.java"} -->Return a copy of the current thread's context map, with keys and values of
        type String. Returned value may be null.
        @return A copy of the current thread's context map. May be null.
        @since 1.5.1

# File: `Logger.java`

## Method: `public void info(String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(String msg)", "entityFile": "Logger.java"} -->Log a message at the INFO level.
        @param msg the message string to be logged

# File: `MDC.java`

## Method: `public static void setContextMap(Map<String, String> contextMap)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void setContextMap(Map<String, String> contextMap)", "entityFile": "MDC.java"} -->Set the current thread's context map by first clearing any existing map and
        then copying the map passed as parameter. The context map passed as
        parameter must only contain keys and values of type String.
        @param contextMap
        must contain only keys and values of type String
        @since 1.5.1

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.util.Collections;
        import java.util.Iterator;
        import java.util.List;
        import java.util.Vector;
        import org.slf4j.Marker;
        /**
        A simple implementation of the Marker interface.
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn
        */
        public class BasicMarker implements Marker {
        private static final long serialVersionUID = 1803952589649545191L;
        private final String name;
        private List<Marker> referenceList;
        BasicMarker(String name) {
        if (name == null) {
        throw new IllegalArgumentException("A marker name cannot be null");
        }
        this.name = name;
        }
        public String getName() {
        return name;
        }
        public synchronized void add(Marker reference) {
        if (reference == null) {
        throw new IllegalArgumentException("A null value cannot be added to a Marker as reference.");
        }
        // no point in adding the reference multiple times
        if (this.contains(reference)) {
        return;
        } else if (reference.contains(this)) {
        // a potential reference should not its future "parent" as a reference
        return;
        } else {
        // let's add the reference
        if (referenceList == null) {
        referenceList = new Vector<Marker>();
        }
        referenceList.add(reference);
        }
        }
        public synchronized boolean hasReferences() {
        return ((referenceList != null) && (referenceList.size() > 0));
        }
        public boolean hasChildren() {
        return hasReferences();
        }
        public synchronized Iterator<Marker> iterator() {
        if (referenceList != null) {
        return referenceList.iterator();
        } else {
        List<Marker> emptyList = Collections.emptyList();
        return emptyList.iterator();
        }
        }
        public synchronized boolean remove(Marker referenceToRemove) {
        if (referenceList == null) {
        return false;
        }
        int size = referenceList.size();
        for (int i = 0; i < size; i++) {
        Marker m = referenceList.get(i);
        if (referenceToRemove.equals(m)) {
        referenceList.remove(i);
        return true;
        }
        }
        return false;
        }
        public boolean contains(Marker other) {
        if (other == null) {
        throw new IllegalArgumentException("Other cannot be null");
        }
        if (this.equals(other)) {
        return true;
        }
        if (hasReferences()) {
        for (Marker ref : referenceList) {
        if (ref.contains(other)) {
        return true;
        }
        }
        }
        return false;
        }
        /**
        This method is mainly used with Expression Evaluators.
        */
        public boolean contains(String name) {
        if (name == null) {
        throw new IllegalArgumentException("Other cannot be null");
        }
        if (this.name.equals(name)) {
        return true;
        }
        if (hasReferences()) {
        for (Marker ref : referenceList) {
        if (ref.contains(name)) {
        return true;
        }
        }
        }
        return false;
        }
        private static String OPEN = "[ ";
        private static String CLOSE = " ]";
        private static String SEP = ", ";
        public boolean equals(Object obj) {
        if (this == obj)
        return true;
        if (obj == null)
        return false;
        if (!(obj instanceof Marker))
        return false;
        final Marker other = (Marker) obj;
        return name.equals(other.getName());
        }
        public int hashCode() {
        return name.hashCode();
        }
        public String toString() {
        if (!this.hasReferences()) {
        return this.getName();
        }
        Iterator<Marker> it = this.iterator();
        Marker reference;
        StringBuilder sb = new StringBuilder(this.getName());
        sb.append(' ').append(OPEN);
        while (it.hasNext()) {
        reference = it.next();
        sb.append(reference.getName());
        if (it.hasNext()) {
        sb.append(SEP);
        }
        }
        sb.append(CLOSE);
        return sb.toString();
        }
        }
        (BasicMarker.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `MDC.java`

## Method: `public static MDCAdapter getMDCAdapter()`

        <!-- META {"entityType": "Method", "entitySignature": "public static MDCAdapter getMDCAdapter()", "entityFile": "MDC.java"} -->Returns the MDCAdapter instance currently in use.
        @return the MDcAdapter instance currently in use.
        @since 1.4.2

# File: `Logger.java`

## Method: `public void info(String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(String format, Object arg)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the INFO level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the INFO level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.util.Map;
        import org.slf4j.spi.MDCAdapter;
        /**
        This adapter is an empty implementation of the MDCAdapter interface.
        It is used for all logging systems which do not support mapped
        diagnostic contexts such as JDK14, simple and NOP.
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1
        */
        public class NOPMDCAdapter implements MDCAdapter {
        public void clear() {
        }
        public String get(String key) {
        return null;
        }
        public void put(String key, String val) {
        }
        public void remove(String key) {
        }
        public Map<String, String> getCopyOfContextMap() {
        return null;
        }
        public void setContextMap(Map<String, String> contextMap) {
        // NOP
        }
        }
        (NOPMDCAdapter.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void info(String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the INFO level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the INFO level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

## Method: `public void info(String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- ae8c9e26-a243-11e9-9f89-333445793454 <=< ACCEPT -->Log a message at the INFO level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the INFO level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for INFO. The variants taking
        #info(String, Object) one and #info(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> ae8c9e26-a243-11e9-9f89-333445793454 -->

## Method: `public void info(String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(String msg, Throwable t)", "entityFile": "Logger.java"} -->Log an exception (throwable) at the INFO level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

# File: `MDC.java`

## Class: `MDC`

        <!-- META {"entityType": "Class", "entitySignature": "MDC", "entityFile": "MDC.java"} -->This class hides and serves as a substitute for the underlying logging
        system's MDC implementation.
        If the underlying logging system offers MDC functionality, then SLF4J's MDC,
        i.e. this class, will delegate to the underlying system's MDC. Note that at
        this time, only two logging systems, namely log4j and logback, offer MDC
        functionality. For java.util.logging which does not support MDC,
        BasicMDCAdapter will be used. For other systems, i.e slf4j-simple
        and slf4j-nop, NOPMDCAdapter will be used.
        Thus, as a SLF4J user, you can take advantage of MDC in the presence of log4j,
        logback, or java.util.logging, but without forcing these systems as
        dependencies upon your users.
        For more information on MDC please see the <a
        href="http://logback.qos.ch/manual/mdc.html">chapter on MDC in the
        logback manual.
        Please note that all methods in this class are static.
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1

# File: `Logger.java`

## Method: `public boolean isInfoEnabled(Marker marker)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isInfoEnabled(Marker marker)", "entityFile": "Logger.java"} --><!-- 6aee5d7e-a244-11e9-8feb-333445793454 <=< ACCEPT -->Similar to #isInfoEnabled() method except that the marker
        data is also taken into consideration.
        @param marker The marker data to take into consideration
        @return true if this logger is warn enabled, false otherwise<!-- ACCEPT >=> 6aee5d7e-a244-11e9-8feb-333445793454 -->

## Method: `public void info(Marker marker, String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(Marker marker, String msg)", "entityFile": "Logger.java"} -->Log a message with the specific Marker at the INFO level.
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged

## Method: `public void info(Marker marker, String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(Marker marker, String format, Object arg)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #info(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void info(Marker marker, String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(Marker marker, String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #info(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `BasicMarkerFactory.java`

## Method: `public BasicMarkerFactory()`

        <!-- META {"entityType": "Method", "entitySignature": "public BasicMarkerFactory()", "entityFile": "BasicMarkerFactory.java"} -->Regular users should not create
        BasicMarkerFactory instances. Marker
        instances can be obtained using the static {@link
        org.slf4j.MarkerFactory#getMarker} method.

## Method: `public Marker getMarker(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public Marker getMarker(String name)", "entityFile": "BasicMarkerFactory.java"} -->Manufacture a BasicMarker instance by name. If the instance has been
        created earlier, return the previously created instance.
        @param name the name of the marker to be created
        @return a Marker instance

## Class: `BasicMarkerFactory`

        <!-- META {"entityType": "Class", "entitySignature": "BasicMarkerFactory", "entityFile": "BasicMarkerFactory.java"} -->An almost trivial implementation of the IMarkerFactory
        interface which creates BasicMarker instances.
        Simple logging systems can conform to the SLF4J API by binding
        org.slf4j.MarkerFactory with an instance of this class.
        @author Ceki G&uuml;lc&uuml;

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        import java.io.Closeable;
        import java.util.Map;
        import org.slf4j.helpers.NOPMDCAdapter;
        import org.slf4j.helpers.BasicMDCAdapter;
        import org.slf4j.helpers.Util;
        import org.slf4j.impl.StaticMDCBinder;
        import org.slf4j.spi.MDCAdapter;
        /**
        This class hides and serves as a substitute for the underlying logging
        system's MDC implementation.
        If the underlying logging system offers MDC functionality, then SLF4J's MDC,
        i.e. this class, will delegate to the underlying system's MDC. Note that at
        this time, only two logging systems, namely log4j and logback, offer MDC
        functionality. For java.util.logging which does not support MDC,
        BasicMDCAdapter will be used. For other systems, i.e slf4j-simple
        and slf4j-nop, NOPMDCAdapter will be used.
        Thus, as a SLF4J user, you can take advantage of MDC in the presence of log4j,
        logback, or java.util.logging, but without forcing these systems as
        dependencies upon your users.
        For more information on MDC please see the <a
        href="http://logback.qos.ch/manual/mdc.html">chapter on MDC in the
        logback manual.
        Please note that all methods in this class are static.
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1
        */
        public class MDC {
        static final String NULL_MDCA_URL = "http://www.slf4j.org/codes.html#null_MDCA";
        static final String NO_STATIC_MDC_BINDER_URL = "http://www.slf4j.org/codes.html#no_static_mdc_binder";
        static MDCAdapter mdcAdapter;
        /**
        An adapter to remove the key when done.
        */
        public static class MDCCloseable implements Closeable {
        private final String key;
        private MDCCloseable(String key) {
        this.key = key;
        }
        public void close() {
        MDC.remove(this.key);
        }
        }
        private MDC() {
        }
        /**
        As of SLF4J version 1.7.14, StaticMDCBinder classes shipping in various bindings
        come with a getSingleton() method. Previously only a public field called SINGLETON
        was available.
        @return MDCAdapter
        @throws NoClassDefFoundError in case no binding is available
        @since 1.7.14
        */
        private static MDCAdapter bwCompatibleGetMDCAdapterFromBinder() throws NoClassDefFoundError {
        try {
        return StaticMDCBinder.getSingleton().getMDCA();
        } catch (NoSuchMethodError nsme) {
        // binding is probably a version of SLF4J older than 1.7.14
        return StaticMDCBinder.SINGLETON.getMDCA();
        }
        }
        static {
        try {
        mdcAdapter = bwCompatibleGetMDCAdapterFromBinder();
        } catch (NoClassDefFoundError ncde) {
        mdcAdapter = new NOPMDCAdapter();
        String msg = ncde.getMessage();
        if (msg != null && msg.contains("StaticMDCBinder")) {
        Util.report("Failed to load class \"org.slf4j.impl.StaticMDCBinder\".");
        Util.report("Defaulting to no-operation MDCAdapter implementation.");
        Util.report("See " + NO_STATIC_MDC_BINDER_URL + " for further details.");
        } else {
        throw ncde;
        }
        } catch (Exception e) {
        // we should never get here
        Util.report("MDC binding unsuccessful.", e);
        }
        }
        /**
        Put a diagnostic context value (the val parameter) as identified with the
        key parameter into the current thread's diagnostic context map. The
        key parameter cannot be null. The val parameter
        can be null only if the underlying implementation supports it.
        This method delegates all work to the MDC of the underlying logging system.
        @param key non-null key
        @param val value to put in the map
        @throws IllegalArgumentException
        in case the "key" parameter is null
        */
        public static void put(String key, String val) throws IllegalArgumentException {
        if (key == null) {
        throw new IllegalArgumentException("key parameter cannot be null");
        }
        if (mdcAdapter == null) {
        throw new IllegalStateException("MDCAdapter cannot be null. See also " + NULL_MDCA_URL);
        }
        mdcAdapter.put(key, val);
        }
        /**
        Put a diagnostic context value (the val parameter) as identified with the
        key parameter into the current thread's diagnostic context map. The
        key parameter cannot be null. The val parameter
        can be null only if the underlying implementation supports it.
        This method delegates all work to the MDC of the underlying logging system.
        This method return a Closeable object who can remove key when
        close is called.
        Useful with Java 7 for example :
        try(MDC.MDCCloseable closeable = MDC.putCloseable(key, value)) {
        ....
        }
        @param key non-null key
        @param val value to put in the map
        @return a Closeable who can remove key when close
        is called.
        @throws IllegalArgumentException
        in case the "key" parameter is null
        */
        public static MDCCloseable putCloseable(String key, String val) throws IllegalArgumentException {
        put(key, val);
        return new MDCCloseable(key);
        }
        /**
        Get the diagnostic context identified by the key parameter. The
        key parameter cannot be null.
        This method delegates all work to the MDC of the underlying logging system.
        @param key
        @return the string value identified by the key parameter.
        @throws IllegalArgumentException
        in case the "key" parameter is null
        */
        public static String get(String key) throws IllegalArgumentException {
        if (key == null) {
        throw new IllegalArgumentException("key parameter cannot be null");
        }
        if (mdcAdapter == null) {
        throw new IllegalStateException("MDCAdapter cannot be null. See also " + NULL_MDCA_URL);
        }
        return mdcAdapter.get(key);
        }
        /**
        Remove the diagnostic context identified by the key parameter using
        the underlying system's MDC implementation. The key parameter
        cannot be null. This method does nothing if there is no previous value
        associated with key.
        @param key
        @throws IllegalArgumentException
        in case the "key" parameter is null
        */
        public static void remove(String key) throws IllegalArgumentException {
        if (key == null) {
        throw new IllegalArgumentException("key parameter cannot be null");
        }
        if (mdcAdapter == null) {
        throw new IllegalStateException("MDCAdapter cannot be null. See also " + NULL_MDCA_URL);
        }
        mdcAdapter.remove(key);
        }
        /**
        Clear all entries in the MDC of the underlying implementation.
        */
        public static void clear() {
        if (mdcAdapter == null) {
        throw new IllegalStateException("MDCAdapter cannot be null. See also " + NULL_MDCA_URL);
        }
        mdcAdapter.clear();
        }
        /**
        Return a copy of the current thread's context map, with keys and values of
        type String. Returned value may be null.
        @return A copy of the current thread's context map. May be null.
        @since 1.5.1
        */
        public static Map<String, String> getCopyOfContextMap() {
        if (mdcAdapter == null) {
        throw new IllegalStateException("MDCAdapter cannot be null. See also " + NULL_MDCA_URL);
        }
        return mdcAdapter.getCopyOfContextMap();
        }
        /**
        Set the current thread's context map by first clearing any existing map and
        then copying the map passed as parameter. The context map passed as
        parameter must only contain keys and values of type String.
        @param contextMap
        must contain only keys and values of type String
        @since 1.5.1
        */
        public static void setContextMap(Map<String, String> contextMap) {
        if (mdcAdapter == null) {
        throw new IllegalStateException("MDCAdapter cannot be null. See also " + NULL_MDCA_URL);
        }
        mdcAdapter.setContextMap(contextMap);
        }
        /**
        Returns the MDCAdapter instance currently in use.
        @return the MDcAdapter instance currently in use.
        @since 1.4.2
        */
        public static MDCAdapter getMDCAdapter() {
        return mdcAdapter;
        }
        }
        (MDC.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public void info(Marker marker, String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(Marker marker, String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #info(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void info(Marker marker, String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void info(Marker marker, String msg, Throwable t)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #info(String, Throwable) method
        except that the marker data is also taken into consideration.
        @param marker the marker data for this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.util.concurrent.ConcurrentHashMap;
        import java.util.concurrent.ConcurrentMap;
        import org.slf4j.IMarkerFactory;
        import org.slf4j.Marker;
        /**
        An almost trivial implementation of the IMarkerFactory
        interface which creates BasicMarker instances.
        Simple logging systems can conform to the SLF4J API by binding
        org.slf4j.MarkerFactory with an instance of this class.
        @author Ceki G&uuml;lc&uuml;
        */
        public class BasicMarkerFactory implements IMarkerFactory {
        private final ConcurrentMap<String, Marker> markerMap = new ConcurrentHashMap<String, Marker>();
        /**
        Regular users should not create
        BasicMarkerFactory instances. Marker
        instances can be obtained using the static {@link
        org.slf4j.MarkerFactory#getMarker} method.
        */
        public BasicMarkerFactory() {
        }
        /**
        Manufacture a BasicMarker instance by name. If the instance has been
        created earlier, return the previously created instance.
        @param name the name of the marker to be created
        @return a Marker instance
        */
        public Marker getMarker(String name) {
        if (name == null) {
        throw new IllegalArgumentException("Marker name cannot be null");
        }
        Marker marker = markerMap.get(name);
        if (marker == null) {
        marker = new BasicMarker(name);
        Marker oldMarker = markerMap.putIfAbsent(name, marker);
        if (oldMarker != null) {
        marker = oldMarker;
        }
        }
        return marker;
        }
        /**
        Does the name marked already exist?
        */
        public boolean exists(String name) {
        if (name == null) {
        return false;
        }
        return markerMap.containsKey(name);
        }
        public boolean detachMarker(String name) {
        if (name == null) {
        return false;
        }
        return (markerMap.remove(name) != null);
        }
        public Marker getDetachedMarker(String name) {
        return new BasicMarker(name);
        }
        }
        (BasicMarkerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Logger.java`

## Method: `public boolean isWarnEnabled()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isWarnEnabled()", "entityFile": "Logger.java"} -->Is the logger instance enabled for the WARN level?
        @return True if this Logger is enabled for the WARN level,
        false otherwise.

## Method: `public void warn(String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(String msg)", "entityFile": "Logger.java"} -->Log a message at the WARN level.
        @param msg the message string to be logged

## Method: `public void warn(String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(String format, Object arg)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the WARN level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the WARN level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

# File: `BasicMDCAdapter.java`

## Method: `public void put(String key, String val)`

        <!-- META {"entityType": "Method", "entitySignature": "public void put(String key, String val)", "entityFile": "BasicMDCAdapter.java"} --><!-- fa1791e4-1793-11ea-a362-333445793454 <=< ACCEPT -->Put a context value (the val parameter) as identified with
        the key parameter into the current thread's context map.
        Note that contrary to log4j, the val parameter can be null.
        If the current thread does not have a context map it is created as a side
        effect of this call.
        @throws IllegalArgumentException
        in case the "key" parameter is null<!-- ACCEPT >=> fa1791e4-1793-11ea-a362-333445793454 -->

## Method: `public String get(String key)`

        <!-- META {"entityType": "Method", "entitySignature": "public String get(String key)", "entityFile": "BasicMDCAdapter.java"} -->Get the context identified by the key parameter.

## Method: `public void remove(String key)`

        <!-- META {"entityType": "Method", "entitySignature": "public void remove(String key)", "entityFile": "BasicMDCAdapter.java"} -->Remove the the context identified by the key parameter.

## Method: `public Set<String> getKeys()`

        <!-- META {"entityType": "Method", "entitySignature": "public Set<String> getKeys()", "entityFile": "BasicMDCAdapter.java"} -->Returns the keys in the MDC as a Set of Strings The
        returned value can be null.
        @return the keys in the MDC

# File: `Logger.java`

## Method: `public void warn(String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- ae8c9e26-a243-11e9-9f89-333445793454 <=< ACCEPT -->Log a message at the WARN level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the WARN level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for WARN. The variants taking
        #warn(String, Object) one and #warn(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> ae8c9e26-a243-11e9-9f89-333445793454 -->

# File: `SubstituteLogger.java`

## Method: `Logger delegate()`

        <!-- META {"entityType": "Method", "entitySignature": "Logger delegate()", "entityFile": "SubstituteLogger.java"} -->Return the delegate logger instance if set. Otherwise, return a NOPLogger
        instance.

# File: `Logger.java`

## Method: `public void warn(String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the WARN level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the WARN level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

# File: `BasicMDCAdapter.java`

## Method: `public Map<String, String> getCopyOfContextMap()`

        <!-- META {"entityType": "Method", "entitySignature": "public Map<String, String> getCopyOfContextMap()", "entityFile": "BasicMDCAdapter.java"} -->Return a copy of the current thread's context map.
        Returned value may be null.

# File: `Logger.java`

## Method: `public void warn(String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(String msg, Throwable t)", "entityFile": "Logger.java"} -->Log an exception (throwable) at the WARN level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

# File: `SubstituteLogger.java`

## Method: `public void setDelegate(Logger delegate)`

        <!-- META {"entityType": "Method", "entitySignature": "public void setDelegate(Logger delegate)", "entityFile": "SubstituteLogger.java"} -->Typically called after the org.slf4j.LoggerFactory initialization phase is completed.
        @param delegate

# File: `BasicMDCAdapter.java`

## Class: `BasicMDCAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "BasicMDCAdapter", "entityFile": "BasicMDCAdapter.java"} -->Basic MDC implementation, which can be used with logging systems that lack
        out-of-the-box MDC support.
        This code was initially inspired by  logback's LogbackMDCAdapter. However,
        LogbackMDCAdapter has evolved and is now considerably more sophisticated.
        @author Ceki Gulcu
        @author Maarten Bosteels
        @author Lukasz Cwik
        @since 1.5.0

# File: `SubstituteLogger.java`

## Class: `SubstituteLogger`

        <!-- META {"entityType": "Class", "entitySignature": "SubstituteLogger", "entityFile": "SubstituteLogger.java"} -->A logger implementation which logs via a delegate logger. By default, the delegate is a
        NOPLogger. However, a different delegate can be set at any time.
        See also the <a href="http://www.slf4j.org/codes.html#substituteLogger">relevant
        error code documentation.
        @author Chetan Mehrotra
        @author Ceki Gulcu

# File: `Logger.java`

## Method: `public boolean isWarnEnabled(Marker marker)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isWarnEnabled(Marker marker)", "entityFile": "Logger.java"} --><!-- 6aee5d7e-a244-11e9-8feb-333445793454 <=< ACCEPT -->Similar to #isWarnEnabled() method except that the marker
        data is also taken into consideration.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the WARN level,
        false otherwise.<!-- ACCEPT >=> 6aee5d7e-a244-11e9-8feb-333445793454 -->

## Method: `public void warn(Marker marker, String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(Marker marker, String msg)", "entityFile": "Logger.java"} -->Log a message with the specific Marker at the WARN level.
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged

## Method: `public void warn(Marker marker, String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(Marker marker, String format, Object arg)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #warn(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void warn(Marker marker, String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(Marker marker, String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #warn(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void warn(Marker marker, String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(Marker marker, String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #warn(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void warn(Marker marker, String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void warn(Marker marker, String msg, Throwable t)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #warn(String, Throwable) method
        except that the marker data is also taken into consideration.
        @param marker the marker data for this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public boolean isErrorEnabled()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isErrorEnabled()", "entityFile": "Logger.java"} -->Is the logger instance enabled for the ERROR level?
        @return True if this Logger is enabled for the ERROR level,
        false otherwise.

## Method: `public void error(String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(String msg)", "entityFile": "Logger.java"} -->Log a message at the ERROR level.
        @param msg the message string to be logged

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import org.slf4j.spi.MDCAdapter;
        import java.util.*;
        import java.util.Map;
        /**
        Basic MDC implementation, which can be used with logging systems that lack
        out-of-the-box MDC support.
        This code was initially inspired by  logback's LogbackMDCAdapter. However,
        LogbackMDCAdapter has evolved and is now considerably more sophisticated.
        @author Ceki Gulcu
        @author Maarten Bosteels
        @author Lukasz Cwik
        @since 1.5.0
        */
        public class BasicMDCAdapter implements MDCAdapter {
        private InheritableThreadLocal<Map<String, String>> inheritableThreadLocal = new InheritableThreadLocal<Map<String, String>>() {
        @Override
        protected Map<String, String> childValue(Map<String, String> parentValue) {
        if (parentValue == null) {
        return null;
        }
        return new HashMap<String, String>(parentValue);
        }
        };
        /**
        Put a context value (the val parameter) as identified with
        the key parameter into the current thread's context map.
        Note that contrary to log4j, the val parameter can be null.
        If the current thread does not have a context map it is created as a side
        effect of this call.
        @throws IllegalArgumentException
        in case the "key" parameter is null
        */
        public void put(String key, String val) {
        if (key == null) {
        throw new IllegalArgumentException("key cannot be null");
        }
        Map<String, String> map = inheritableThreadLocal.get();
        if (map == null) {
        map = new HashMap<String, String>();
        inheritableThreadLocal.set(map);
        }
        map.put(key, val);
        }
        /**
        Get the context identified by the key parameter.
        */
        public String get(String key) {
        Map<String, String> map = inheritableThreadLocal.get();
        if ((map != null) && (key != null)) {
        return map.get(key);
        } else {
        return null;
        }
        }
        /**
        Remove the the context identified by the key parameter.
        */
        public void remove(String key) {
        Map<String, String> map = inheritableThreadLocal.get();
        if (map != null) {
        map.remove(key);
        }
        }
        /**
        Clear all entries in the MDC.
        */
        public void clear() {
        Map<String, String> map = inheritableThreadLocal.get();
        if (map != null) {
        map.clear();
        inheritableThreadLocal.remove();
        }
        }
        /**
        Returns the keys in the MDC as a Set of Strings The
        returned value can be null.
        @return the keys in the MDC
        */
        public Set<String> getKeys() {
        Map<String, String> map = inheritableThreadLocal.get();
        if (map != null) {
        return map.keySet();
        } else {
        return null;
        }
        }
        /**
        Return a copy of the current thread's context map.
        Returned value may be null.
        */
        public Map<String, String> getCopyOfContextMap() {
        Map<String, String> oldMap = inheritableThreadLocal.get();
        if (oldMap != null) {
        return new HashMap<String, String>(oldMap);
        } else {
        return null;
        }
        }
        public void setContextMap(Map<String, String> contextMap) {
        inheritableThreadLocal.set(new HashMap<String, String>(contextMap));
        }
        }
        (BasicMDCAdapter.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `LoggerFactory.java`

## Field: `API_COMPATIBILITY_LIST`

        <!-- META {"entityType": "Field", "entitySignature": "API_COMPATIBILITY_LIST", "entityFile": "LoggerFactory.java"} -->It is LoggerFactory's responsibility to track version changes and manage
        the compatibility list.
        It is assumed that all versions in the 1.6 are mutually compatible.

# File: `Logger.java`

## Method: `public void error(String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(String format, Object arg)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the ERROR level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the ERROR level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

## Method: `public void error(String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the ERROR level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the ERROR level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->

# File: `LoggerFactory.java`

## Method: `static void reset()`

        <!-- META {"entityType": "Method", "entitySignature": "static void reset()", "entityFile": "LoggerFactory.java"} -->Force LoggerFactory to consider itself uninitialized.
        This method is intended to be called by classes (in the same package) for
        testing purposes. This method is internal. It can be modified, renamed or
        removed at any time without notice.
        You are strongly discouraged from calling this method in production code.

## Method: `private static void reportMultipleBindingAmbiguity(Set<URL> binderPathSet)`

        <!-- META {"entityType": "Method", "entitySignature": "private static void reportMultipleBindingAmbiguity(Set<URL> binderPathSet)", "entityFile": "LoggerFactory.java"} -->Prints a warning message on the console if multiple bindings were found on the class path.
        No reporting is done otherwise.

# File: `Logger.java`

## Method: `public void error(String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- ae8c9e26-a243-11e9-9f89-333445793454 <=< ACCEPT -->Log a message at the ERROR level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the ERROR level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for ERROR. The variants taking
        #error(String, Object) one and #error(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> ae8c9e26-a243-11e9-9f89-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import java.lang.reflect.InvocationTargetException;
        import java.lang.reflect.Method;
        import java.util.Queue;
        import org.slf4j.Logger;
        import org.slf4j.Marker;
        import org.slf4j.event.EventRecodingLogger;
        import org.slf4j.event.LoggingEvent;
        import org.slf4j.event.SubstituteLoggingEvent;
        /**
        A logger implementation which logs via a delegate logger. By default, the delegate is a
        NOPLogger. However, a different delegate can be set at any time.
        See also the <a href="http://www.slf4j.org/codes.html#substituteLogger">relevant
        error code documentation.
        @author Chetan Mehrotra
        @author Ceki Gulcu
        */
        public class SubstituteLogger implements Logger {
        private final String name;
        private volatile Logger _delegate;
        private Boolean delegateEventAware;
        private Method logMethodCache;
        private EventRecodingLogger eventRecodingLogger;
        private Queue<SubstituteLoggingEvent> eventQueue;
        public SubstituteLogger(String name, Queue<SubstituteLoggingEvent> eventQueue) {
        this.name = name;
        this.eventQueue = eventQueue;
        }
        public String getName() {
        return name;
        }
        public boolean isTraceEnabled() {
        return delegate().isTraceEnabled();
        }
        public void trace(String msg) {
        delegate().trace(msg);
        }
        public void trace(String format, Object arg) {
        delegate().trace(format, arg);
        }
        public void trace(String format, Object arg1, Object arg2) {
        delegate().trace(format, arg1, arg2);
        }
        public void trace(String format, Object... arguments) {
        delegate().trace(format, arguments);
        }
        public void trace(String msg, Throwable t) {
        delegate().trace(msg, t);
        }
        public boolean isTraceEnabled(Marker marker) {
        return delegate().isTraceEnabled(marker);
        }
        public void trace(Marker marker, String msg) {
        delegate().trace(marker, msg);
        }
        public void trace(Marker marker, String format, Object arg) {
        delegate().trace(marker, format, arg);
        }
        public void trace(Marker marker, String format, Object arg1, Object arg2) {
        delegate().trace(marker, format, arg1, arg2);
        }
        public void trace(Marker marker, String format, Object... arguments) {
        delegate().trace(marker, format, arguments);
        }
        public void trace(Marker marker, String msg, Throwable t) {
        delegate().trace(marker, msg, t);
        }
        public boolean isDebugEnabled() {
        return delegate().isDebugEnabled();
        }
        public void debug(String msg) {
        delegate().debug(msg);
        }
        public void debug(String format, Object arg) {
        delegate().debug(format, arg);
        }
        public void debug(String format, Object arg1, Object arg2) {
        delegate().debug(format, arg1, arg2);
        }
        public void debug(String format, Object... arguments) {
        delegate().debug(format, arguments);
        }
        public void debug(String msg, Throwable t) {
        delegate().debug(msg, t);
        }
        public boolean isDebugEnabled(Marker marker) {
        return delegate().isDebugEnabled(marker);
        }
        public void debug(Marker marker, String msg) {
        delegate().debug(marker, msg);
        }
        public void debug(Marker marker, String format, Object arg) {
        delegate().debug(marker, format, arg);
        }
        public void debug(Marker marker, String format, Object arg1, Object arg2) {
        delegate().debug(marker, format, arg1, arg2);
        }
        public void debug(Marker marker, String format, Object... arguments) {
        delegate().debug(marker, format, arguments);
        }
        public void debug(Marker marker, String msg, Throwable t) {
        delegate().debug(marker, msg, t);
        }
        public boolean isInfoEnabled() {
        return delegate().isInfoEnabled();
        }
        public void info(String msg) {
        delegate().info(msg);
        }
        public void info(String format, Object arg) {
        delegate().info(format, arg);
        }
        public void info(String format, Object arg1, Object arg2) {
        delegate().info(format, arg1, arg2);
        }
        public void info(String format, Object... arguments) {
        delegate().info(format, arguments);
        }
        public void info(String msg, Throwable t) {
        delegate().info(msg, t);
        }
        public boolean isInfoEnabled(Marker marker) {
        return delegate().isInfoEnabled(marker);
        }
        public void info(Marker marker, String msg) {
        delegate().info(marker, msg);
        }
        public void info(Marker marker, String format, Object arg) {
        delegate().info(marker, format, arg);
        }
        public void info(Marker marker, String format, Object arg1, Object arg2) {
        delegate().info(marker, format, arg1, arg2);
        }
        public void info(Marker marker, String format, Object... arguments) {
        delegate().info(marker, format, arguments);
        }
        public void info(Marker marker, String msg, Throwable t) {
        delegate().info(marker, msg, t);
        }
        public boolean isWarnEnabled() {
        return delegate().isWarnEnabled();
        }
        public void warn(String msg) {
        delegate().warn(msg);
        }
        public void warn(String format, Object arg) {
        delegate().warn(format, arg);
        }
        public void warn(String format, Object arg1, Object arg2) {
        delegate().warn(format, arg1, arg2);
        }
        public void warn(String format, Object... arguments) {
        delegate().warn(format, arguments);
        }
        public void warn(String msg, Throwable t) {
        delegate().warn(msg, t);
        }
        public boolean isWarnEnabled(Marker marker) {
        return delegate().isWarnEnabled(marker);
        }
        public void warn(Marker marker, String msg) {
        delegate().warn(marker, msg);
        }
        public void warn(Marker marker, String format, Object arg) {
        delegate().warn(marker, format, arg);
        }
        public void warn(Marker marker, String format, Object arg1, Object arg2) {
        delegate().warn(marker, format, arg1, arg2);
        }
        public void warn(Marker marker, String format, Object... arguments) {
        delegate().warn(marker, format, arguments);
        }
        public void warn(Marker marker, String msg, Throwable t) {
        delegate().warn(marker, msg, t);
        }
        public boolean isErrorEnabled() {
        return delegate().isErrorEnabled();
        }
        public void error(String msg) {
        delegate().error(msg);
        }
        public void error(String format, Object arg) {
        delegate().error(format, arg);
        }
        public void error(String format, Object arg1, Object arg2) {
        delegate().error(format, arg1, arg2);
        }
        public void error(String format, Object... arguments) {
        delegate().error(format, arguments);
        }
        public void error(String msg, Throwable t) {
        delegate().error(msg, t);
        }
        public boolean isErrorEnabled(Marker marker) {
        return delegate().isErrorEnabled(marker);
        }
        public void error(Marker marker, String msg) {
        delegate().error(marker, msg);
        }
        public void error(Marker marker, String format, Object arg) {
        delegate().error(marker, format, arg);
        }
        public void error(Marker marker, String format, Object arg1, Object arg2) {
        delegate().error(marker, format, arg1, arg2);
        }
        public void error(Marker marker, String format, Object... arguments) {
        delegate().error(marker, format, arguments);
        }
        public void error(Marker marker, String msg, Throwable t) {
        delegate().error(marker, msg, t);
        }
        @Override
        public boolean equals(Object o) {
        if (this == o)
        return true;
        if (o == null || getClass() != o.getClass())
        return false;
        SubstituteLogger that = (SubstituteLogger) o;
        if (!name.equals(that.name))
        return false;
        return true;
        }
        @Override
        public int hashCode() {
        return name.hashCode();
        }
        /**
        Return the delegate logger instance if set. Otherwise, return a NOPLogger
        instance.
        */
        Logger delegate() {
        return _delegate != null ? _delegate : getEventRecordingLogger();
        }
        private Logger getEventRecordingLogger() {
        if (eventRecodingLogger == null) {
        eventRecodingLogger = new EventRecodingLogger(this, eventQueue);
        }
        return eventRecodingLogger;
        }
        /**
        Typically called after the org.slf4j.LoggerFactory initialization phase is completed.
        @param delegate
        */
        public void setDelegate(Logger delegate) {
        this._delegate = delegate;
        }
        public boolean isDelegateEventAware() {
        if (delegateEventAware != null)
        return delegateEventAware;
        try {
        logMethodCache = _delegate.getClass().getMethod("log", LoggingEvent.class);
        delegateEventAware = Boolean.TRUE;
        } catch (NoSuchMethodException e) {
        delegateEventAware = Boolean.FALSE;
        }
        return delegateEventAware;
        }
        public void log(LoggingEvent event) {
        if (isDelegateEventAware()) {
        try {
        logMethodCache.invoke(_delegate, event);
        } catch (IllegalAccessException e) {
        } catch (IllegalArgumentException e) {
        } catch (InvocationTargetException e) {
        }
        }
        }
        public boolean isDelegateNull() {
        return _delegate == null;
        }
        public boolean isDelegateNOP() {
        return _delegate instanceof NOPLogger;
        }
        }
        (SubstituteLogger.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `LoggerFactory.java`

## Method: `public static Logger getLogger(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Logger getLogger(String name)", "entityFile": "LoggerFactory.java"} -->Return a logger named according to the name parameter using the statically
        bound ILoggerFactory instance.
        @param name The name of the logger.
        @return logger

## Method: `public static Logger getLogger(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Logger getLogger(Class<?> clazz)", "entityFile": "LoggerFactory.java"} -->Return a logger named corresponding to the class passed as parameter, using
        the statically bound ILoggerFactory instance.
        In case the the clazz parameter differs from the name of
        the caller as computed internally by SLF4J, a logger name mismatch warning will be
        printed but only if the slf4j.detectLoggerNameMismatch system property is
        set to true. By default, this property is not set and no warnings will be printed
        even in case of a logger name mismatch.
        @param clazz the returned logger will be named after clazz
        @return logger
        @see <a href="http://www.slf4j.org/codes.html#loggerNameMismatch">Detected logger name mismatch

## Method: `public static ILoggerFactory getILoggerFactory()`

        <!-- META {"entityType": "Method", "entitySignature": "public static ILoggerFactory getILoggerFactory()", "entityFile": "LoggerFactory.java"} -->Return the ILoggerFactory instance in use.
        ILoggerFactory instance is bound with this class at compile time.
        @return the ILoggerFactory instance in use

## Class: `LoggerFactory`

        <!-- META {"entityType": "Class", "entitySignature": "LoggerFactory", "entityFile": "LoggerFactory.java"} -->The LoggerFactory is a utility class producing Loggers for
        various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
        Other implementations such as org.slf4j.impl.NOPLogger NOPLogger and
        org.slf4j.impl.SimpleLogger SimpleLogger are also supported.
        LoggerFactory is essentially a wrapper around an
        ILoggerFactory instance bound with LoggerFactory at
        compile time.
        Please note that all methods in LoggerFactory are static.
        @author Alexander Dorokhine
        @author Robert Elliot
        @author Ceki G&uuml;lc&uuml;

# File: `Logger.java`

## Method: `public void error(String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(String msg, Throwable t)", "entityFile": "Logger.java"} -->Log an exception (throwable) at the ERROR level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

## Method: `public boolean isErrorEnabled(Marker marker)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isErrorEnabled(Marker marker)", "entityFile": "Logger.java"} --><!-- 6aee5d7e-a244-11e9-8feb-333445793454 <=< ACCEPT -->Similar to #isErrorEnabled() method except that the
        marker data is also taken into consideration.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the ERROR level,
        false otherwise.<!-- ACCEPT >=> 6aee5d7e-a244-11e9-8feb-333445793454 -->

## Method: `public void error(Marker marker, String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(Marker marker, String msg)", "entityFile": "Logger.java"} --><!-- e5db5ac6-1796-11ea-84d9-333445793454 <=< ACCEPT -->Log a message with the specific Marker at the ERROR level.
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged<!-- ACCEPT >=> e5db5ac6-1796-11ea-84d9-333445793454 -->

## Method: `public void error(Marker marker, String format, Object arg)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(Marker marker, String format, Object arg)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #error(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void error(Marker marker, String format, Object arg1, Object arg2)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(Marker marker, String format, Object arg1, Object arg2)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #error(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

## Method: `public void error(Marker marker, String format, Object... arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(Marker marker, String format, Object... arguments)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #error(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `NOPLogger.java`

## Method: `protected NOPLogger()`

        <!-- META {"entityType": "Method", "entitySignature": "protected NOPLogger()", "entityFile": "NOPLogger.java"} -->There is no point in creating multiple instances of NOPLOgger,
        except by derived classes, hence the protected  access for the constructor.

# File: `Logger.java`

## Method: `public void error(Marker marker, String msg, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public void error(Marker marker, String msg, Throwable t)", "entityFile": "Logger.java"} --><!-- c4180674-1790-11ea-915f-333445793454 <=< ACCEPT -->This method is similar to #error(String, Throwable)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log<!-- ACCEPT >=> c4180674-1790-11ea-915f-333445793454 -->

# File: `NOPLogger.java`

## Class: `NOPLogger`

        <!-- META {"entityType": "Class", "entitySignature": "NOPLogger", "entityFile": "NOPLogger.java"} -->A direct NOP (no operation) implementation of Logger.
        @author Ceki G&uuml;lc&uuml;

# File: `Logger.java`

## Interface: `Logger`

        <!-- META {"entityType": "Interface", "entitySignature": "Logger", "entityFile": "Logger.java"} -->The org.slf4j.Logger interface is the main user entry point of SLF4J API.
        It is expected that logging takes place through concrete implementations
        of this interface.
        Typical usage pattern:
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        public class Wombat {
        <span style="color:green">final static Logger logger = LoggerFactory.getLogger(Wombat.class);
        Integer t;
        Integer oldT;
        public void setTemperature(Integer temperature) {
        oldT = t;
        t = temperature;
        <span style="color:green">logger.debug("Temperature set to {}. Old temperature was {}.", t, oldT);
        if(temperature.intValue() > 50) {
        <span style="color:green">logger.info("Temperature has risen above 50 degrees.");
        }
        }
        }
        Be sure to read the FAQ entry relating to <a href="../../../faq.html#logging_performance">parameterized
        logging. Note that logging statements can be parameterized in
        <a href="../../../faq.html#paramException">presence of an exception/throwable.
        Once you are comfortable using loggers, i.e. instances of this interface, consider using
        <a href="MDC.html">MDC as well as <a href="Marker.html">Markers.
        @author Ceki G&uuml;lc&uuml;

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        import java.io.IOException;
        import java.net.URL;
        import java.util.ArrayList;
        import java.util.Arrays;
        import java.util.Enumeration;
        import java.util.LinkedHashSet;
        import java.util.List;
        import java.util.Set;
        import java.util.concurrent.LinkedBlockingQueue;
        import org.slf4j.event.SubstituteLoggingEvent;
        import org.slf4j.helpers.NOPLoggerFactory;
        import org.slf4j.helpers.SubstituteLogger;
        import org.slf4j.helpers.SubstituteLoggerFactory;
        import org.slf4j.helpers.Util;
        import org.slf4j.impl.StaticLoggerBinder;
        /**
        The LoggerFactory is a utility class producing Loggers for
        various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
        Other implementations such as org.slf4j.impl.NOPLogger NOPLogger and
        org.slf4j.impl.SimpleLogger SimpleLogger are also supported.
        LoggerFactory is essentially a wrapper around an
        ILoggerFactory instance bound with LoggerFactory at
        compile time.
        Please note that all methods in LoggerFactory are static.
        @author Alexander Dorokhine
        @author Robert Elliot
        @author Ceki G&uuml;lc&uuml;
        */
        public final class LoggerFactory {
        static final String CODES_PREFIX = "http://www.slf4j.org/codes.html";
        static final String NO_STATICLOGGERBINDER_URL = CODES_PREFIX + "#StaticLoggerBinder";
        static final String MULTIPLE_BINDINGS_URL = CODES_PREFIX + "#multiple_bindings";
        static final String NULL_LF_URL = CODES_PREFIX + "#null_LF";
        static final String VERSION_MISMATCH = CODES_PREFIX + "#version_mismatch";
        static final String SUBSTITUTE_LOGGER_URL = CODES_PREFIX + "#substituteLogger";
        static final String LOGGER_NAME_MISMATCH_URL = CODES_PREFIX + "#loggerNameMismatch";
        static final String REPLAY_URL = CODES_PREFIX + "#replay";
        static final String UNSUCCESSFUL_INIT_URL = CODES_PREFIX + "#unsuccessfulInit";
        static final String UNSUCCESSFUL_INIT_MSG = "org.slf4j.LoggerFactory could not be successfully initialized. See also " + UNSUCCESSFUL_INIT_URL;
        static final int UNINITIALIZED = 0;
        static final int ONGOING_INITIALIZATION = 1;
        static final int FAILED_INITIALIZATION = 2;
        static final int SUCCESSFUL_INITIALIZATION = 3;
        static final int NOP_FALLBACK_INITIALIZATION = 4;
        static volatile int INITIALIZATION_STATE = UNINITIALIZED;
        static SubstituteLoggerFactory SUBST_FACTORY = new SubstituteLoggerFactory();
        static NOPLoggerFactory NOP_FALLBACK_FACTORY = new NOPLoggerFactory();
        // Support for detecting mismatched logger names.
        static final String DETECT_LOGGER_NAME_MISMATCH_PROPERTY = "slf4j.detectLoggerNameMismatch";
        static final String JAVA_VENDOR_PROPERTY = "java.vendor.url";
        static boolean DETECT_LOGGER_NAME_MISMATCH = Util.safeGetBooleanSystemProperty(DETECT_LOGGER_NAME_MISMATCH_PROPERTY);
        /**
        It is LoggerFactory's responsibility to track version changes and manage
        the compatibility list.
        It is assumed that all versions in the 1.6 are mutually compatible.
        */
        private static final String[] API_COMPATIBILITY_LIST = new String[] { "1.6", "1.7" };
        // private constructor prevents instantiation
        private LoggerFactory() {
        }
        /**
        Force LoggerFactory to consider itself uninitialized.
        This method is intended to be called by classes (in the same package) for
        testing purposes. This method is internal. It can be modified, renamed or
        removed at any time without notice.
        You are strongly discouraged from calling this method in production code.
        */
        static void reset() {
        INITIALIZATION_STATE = UNINITIALIZED;
        }
        private static final void performInitialization() {
        bind();
        if (INITIALIZATION_STATE == SUCCESSFUL_INITIALIZATION) {
        versionSanityCheck();
        }
        }
        private static boolean messageContainsOrgSlf4jImplStaticLoggerBinder(String msg) {
        if (msg == null)
        return false;
        if (msg.contains("org/slf4j/impl/StaticLoggerBinder"))
        return true;
        if (msg.contains("org.slf4j.impl.StaticLoggerBinder"))
        return true;
        return false;
        }
        private static final void bind() {
        try {
        Set<URL> staticLoggerBinderPathSet = null;
        // skip check under android, see also http://jira.qos.ch/browse/SLF4J-328
        if (!isAndroid()) {
        staticLoggerBinderPathSet = findPossibleStaticLoggerBinderPathSet();
        reportMultipleBindingAmbiguity(staticLoggerBinderPathSet);
        }
        // the next line does the binding
        StaticLoggerBinder.getSingleton();
        INITIALIZATION_STATE = SUCCESSFUL_INITIALIZATION;
        reportActualBinding(staticLoggerBinderPathSet);
        replayEvents();
        } catch (NoClassDefFoundError ncde) {
        String msg = ncde.getMessage();
        if (messageContainsOrgSlf4jImplStaticLoggerBinder(msg)) {
        INITIALIZATION_STATE = NOP_FALLBACK_INITIALIZATION;
        Util.report("Failed to load class \"org.slf4j.impl.StaticLoggerBinder\".");
        Util.report("Defaulting to no-operation (NOP) logger implementation");
        Util.report("See " + NO_STATICLOGGERBINDER_URL + " for further details.");
        } else {
        failedBinding(ncde);
        throw ncde;
        }
        } catch (java.lang.NoSuchMethodError nsme) {
        String msg = nsme.getMessage();
        if (msg != null && msg.contains("org.slf4j.impl.StaticLoggerBinder.getSingleton()")) {
        INITIALIZATION_STATE = FAILED_INITIALIZATION;
        Util.report("slf4j-api 1.6.x (or later) is incompatible with this binding.");
        Util.report("Your binding is version 1.5.5 or earlier.");
        Util.report("Upgrade your binding to version 1.6.x.");
        }
        throw nsme;
        } catch (Exception e) {
        failedBinding(e);
        throw new IllegalStateException("Unexpected initialization failure", e);
        }
        }
        static void failedBinding(Throwable t) {
        INITIALIZATION_STATE = FAILED_INITIALIZATION;
        Util.report("Failed to instantiate SLF4J LoggerFactory", t);
        }
        private static void replayEvents() {
        final LinkedBlockingQueue<SubstituteLoggingEvent> queue = SUBST_FACTORY.getEventQueue();
        final int queueSize = queue.size();
        int count = 0;
        final int maxDrain = 128;
        List<SubstituteLoggingEvent> eventList = new ArrayList<SubstituteLoggingEvent>(maxDrain);
        while (true) {
        int numDrained = queue.drainTo(eventList, maxDrain);
        if (numDrained == 0)
        break;
        for (SubstituteLoggingEvent event : eventList) {
        replaySingleEvent(event);
        if (count++ == 0)
        emitReplayOrSubstituionWarning(event, queueSize);
        }
        eventList.clear();
        }
        }
        private static void emitReplayOrSubstituionWarning(SubstituteLoggingEvent event, int queueSize) {
        if (event.getLogger().isDelegateEventAware()) {
        emitReplayWarning(queueSize);
        } else if (event.getLogger().isDelegateNOP()) {
        // nothing to do
        } else {
        emitSubstitutionWarning();
        }
        }
        private static void replaySingleEvent(SubstituteLoggingEvent event) {
        if (event == null)
        return;
        SubstituteLogger substLogger = event.getLogger();
        String loggerName = substLogger.getName();
        if (substLogger.isDelegateNull()) {
        Logger logger = getLogger(loggerName);
        substLogger.setDelegate(logger);
        }
        if (substLogger.isDelegateNOP()) {
        // nothing to do
        } else if (substLogger.isDelegateEventAware()) {
        substLogger.log(event);
        } else {
        Util.report(loggerName);
        }
        }
        private static void emitSubstitutionWarning() {
        Util.report("The following set of substitute loggers may have been accessed");
        Util.report("during the initialization phase. Logging calls during this");
        Util.report("phase were not honored. However, subsequent logging calls to these");
        Util.report("loggers will work as normally expected.");
        Util.report("See also " + SUBSTITUTE_LOGGER_URL);
        }
        private static void emitReplayWarning(int eventCount) {
        Util.report("A number (" + eventCount + ") of logging calls during the initialization phase have been intercepted and are");
        Util.report("now being replayed. These are suject to the filtering rules of the underlying logging system.");
        Util.report("See also " + REPLAY_URL);
        }
        private static final void versionSanityCheck() {
        try {
        String requested = StaticLoggerBinder.REQUESTED_API_VERSION;
        boolean match = false;
        for (String aAPI_COMPATIBILITY_LIST : API_COMPATIBILITY_LIST) {
        if (requested.startsWith(aAPI_COMPATIBILITY_LIST)) {
        match = true;
        }
        }
        if (!match) {
        Util.report("The requested version " + requested + " by your slf4j binding is not compatible with " + Arrays.asList(API_COMPATIBILITY_LIST).toString());
        Util.report("See " + VERSION_MISMATCH + " for further details.");
        }
        } catch (java.lang.NoSuchFieldError nsfe) {
        // given our large user base and SLF4J's commitment to backward
        // compatibility, we cannot cry here. Only for implementations
        // which willingly declare a REQUESTED_API_VERSION field do we
        // emit compatibility warnings.
        } catch (Throwable e) {
        // we should never reach here
        Util.report("Unexpected problem occured during version sanity check", e);
        }
        }
        // We need to use the name of the StaticLoggerBinder class, but we can't reference
        // the class itself.
        private static String STATIC_LOGGER_BINDER_PATH = "org/slf4j/impl/StaticLoggerBinder.class";
        static Set<URL> findPossibleStaticLoggerBinderPathSet() {
        // use Set instead of list in order to deal with bug #138
        // LinkedHashSet appropriate here because it preserves insertion order during iteration
        Set<URL> staticLoggerBinderPathSet = new LinkedHashSet<URL>();
        try {
        # Class Loader loggerFactoryClassLoader = LoggerFactory.class.getClassLoader();
        Enumeration<URL> paths;
        if (loggerFactoryClassLoader == null) {
        paths = ClassLoader.getSystemResources(STATIC_LOGGER_BINDER_PATH);
        } else {
        paths = loggerFactoryClassLoader.getResources(STATIC_LOGGER_BINDER_PATH);
        }
        while (paths.hasMoreElements()) {
        URL path = paths.nextElement();
        staticLoggerBinderPathSet.add(path);
        }
        } catch (IOException ioe) {
        Util.report("Error getting resources from path", ioe);
        }
        return staticLoggerBinderPathSet;
        }
        private static boolean isAmbiguousStaticLoggerBinderPathSet(Set<URL> binderPathSet) {
        return binderPathSet.size() > 1;
        }
        /**
        Prints a warning message on the console if multiple bindings were found on the class path.
        No reporting is done otherwise.
        */
        private static void reportMultipleBindingAmbiguity(Set<URL> binderPathSet) {
        if (isAmbiguousStaticLoggerBinderPathSet(binderPathSet)) {
        Util.report("Class path contains multiple SLF4J bindings.");
        for (URL path : binderPathSet) {
        Util.report("Found binding in [" + path + "]");
        }
        Util.report("See " + MULTIPLE_BINDINGS_URL + " for an explanation.");
        }
        }
        private static boolean isAndroid() {
        String vendor = Util.safeGetSystemProperty(JAVA_VENDOR_PROPERTY);
        if (vendor == null)
        return false;
        return vendor.toLowerCase().contains("android");
        }
        private static void reportActualBinding(Set<URL> binderPathSet) {
        // binderPathSet can be null under Android
        if (binderPathSet != null && isAmbiguousStaticLoggerBinderPathSet(binderPathSet)) {
        Util.report("Actual binding is of type [" + StaticLoggerBinder.getSingleton().getLoggerFactoryClassStr() + "]");
        }
        }
        /**
        Return a logger named according to the name parameter using the statically
        bound ILoggerFactory instance.
        @param name The name of the logger.
        @return logger
        */
        public static Logger getLogger(String name) {
        ILoggerFactory iLoggerFactory = getILoggerFactory();
        return iLoggerFactory.getLogger(name);
        }
        /**
        Return a logger named corresponding to the class passed as parameter, using
        the statically bound ILoggerFactory instance.
        In case the the clazz parameter differs from the name of
        the caller as computed internally by SLF4J, a logger name mismatch warning will be
        printed but only if the slf4j.detectLoggerNameMismatch system property is
        set to true. By default, this property is not set and no warnings will be printed
        even in case of a logger name mismatch.
        @param clazz the returned logger will be named after clazz
        @return logger
        @see <a href="http://www.slf4j.org/codes.html#loggerNameMismatch">Detected logger name mismatch
        */
        public static Logger getLogger(Class<?> clazz) {
        Logger logger = getLogger(clazz.getName());
        if (DETECT_LOGGER_NAME_MISMATCH) {
        # Class <?> autoComputedCallingClass = Util.getCallingClass();
        if (autoComputedCallingClass != null && nonMatchingClasses(clazz, autoComputedCallingClass)) {
        Util.report(String.format("Detected logger name mismatch. Given name: \"%s\"; computed name: \"%s\".", logger.getName(), autoComputedCallingClass.getName()));
        Util.report("See " + LOGGER_NAME_MISMATCH_URL + " for an explanation");
        }
        }
        return logger;
        }
        private static boolean nonMatchingClasses(Class<?> clazz, Class<?> autoComputedCallingClass) {
        return !autoComputedCallingClass.isAssignableFrom(clazz);
        }
        /**
        Return the ILoggerFactory instance in use.
        ILoggerFactory instance is bound with this class at compile time.
        @return the ILoggerFactory instance in use
        */
        public static ILoggerFactory getILoggerFactory() {
        if (INITIALIZATION_STATE == UNINITIALIZED) {
        synchronized (LoggerFactory.class) {
        if (INITIALIZATION_STATE == UNINITIALIZED) {
        INITIALIZATION_STATE = ONGOING_INITIALIZATION;
        performInitialization();
        }
        }
        }
        switch(INITIALIZATION_STATE) {
        case SUCCESSFUL_INITIALIZATION:
        return StaticLoggerBinder.getSingleton().getLoggerFactory();
        case NOP_FALLBACK_INITIALIZATION:
        return NOP_FALLBACK_FACTORY;
        case FAILED_INITIALIZATION:
        throw new IllegalStateException(UNSUCCESSFUL_INIT_MSG);
        case ONGOING_INITIALIZATION:
        // See also http://jira.qos.ch/browse/SLF4J-97
        return SUBST_FACTORY;
        }
        throw new IllegalStateException("Unreachable code");
        }
        }
        (LoggerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        <!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Marker.java`

## Method: `public String getName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getName()", "entityFile": "Marker.java"} -->Get the name of this Marker.
        @return name of marker

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j.helpers;
        import org.slf4j.Logger;
        import org.slf4j.helpers.MarkerIgnoringBase;
        /**
        A direct NOP (no operation) implementation of Logger.
        @author Ceki G&uuml;lc&uuml;
        */
        public class NOPLogger extends MarkerIgnoringBase {
        private static final long serialVersionUID = -517220405410904473L;
        /**
        The unique instance of NOPLogger.
        */
        public static final NOPLogger NOP_LOGGER = new NOPLogger();
        /**
        There is no point in creating multiple instances of NOPLOgger,
        except by derived classes, hence the protected  access for the constructor.
        */
        protected NOPLogger() {
        }
        /**
        Always returns the string value "NOP".
        */
        public String getName() {
        return "NOP";
        }
        /**
        <!-- 76668dc0-1797-11ea-92be-333445793454 <=< ACCEPT -->Always returns false.
        @return always false<!-- ACCEPT >=> 76668dc0-1797-11ea-92be-333445793454 -->
        */
        public final boolean isTraceEnabled() {
        return false;
        }
        /**
        A NOP implementation.
        */
        public final void trace(String msg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void trace(String format, Object arg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void trace(String format, Object arg1, Object arg2) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void trace(String format, Object... argArray) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void trace(String msg, Throwable t) {
        // NOP
        }
        /**
        <!-- 76668dc0-1797-11ea-92be-333445793454 <=< ACCEPT -->Always returns false.
        @return always false<!-- ACCEPT >=> 76668dc0-1797-11ea-92be-333445793454 -->
        */
        public final boolean isDebugEnabled() {
        return false;
        }
        /**
        A NOP implementation.
        */
        public final void debug(String msg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void debug(String format, Object arg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void debug(String format, Object arg1, Object arg2) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void debug(String format, Object... argArray) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void debug(String msg, Throwable t) {
        // NOP
        }
        /**
        <!-- 76668dc0-1797-11ea-92be-333445793454 <=< ACCEPT -->Always returns false.
        @return always false<!-- ACCEPT >=> 76668dc0-1797-11ea-92be-333445793454 -->
        */
        public final boolean isInfoEnabled() {
        // NOP
        return false;
        }
        /**
        A NOP implementation.
        */
        public final void info(String msg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void info(String format, Object arg1) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void info(String format, Object arg1, Object arg2) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void info(String format, Object... argArray) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void info(String msg, Throwable t) {
        // NOP
        }
        /**
        <!-- 76668dc0-1797-11ea-92be-333445793454 <=< ACCEPT -->Always returns false.
        @return always false<!-- ACCEPT >=> 76668dc0-1797-11ea-92be-333445793454 -->
        */
        public final boolean isWarnEnabled() {
        return false;
        }
        /**
        A NOP implementation.
        */
        public final void warn(String msg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void warn(String format, Object arg1) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void warn(String format, Object arg1, Object arg2) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void warn(String format, Object... argArray) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void warn(String msg, Throwable t) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final boolean isErrorEnabled() {
        return false;
        }
        /**
        A NOP implementation.
        */
        public final void error(String msg) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void error(String format, Object arg1) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void error(String format, Object arg1, Object arg2) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void error(String format, Object... argArray) {
        // NOP
        }
        /**
        A NOP implementation.
        */
        public final void error(String msg, Throwable t) {
        // NOP
        }
        }
        (NOPLogger.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `NOPLoggerFactory.java`

## Class: `NOPLoggerFactory`

        <!-- META {"entityType": "Class", "entitySignature": "NOPLoggerFactory", "entityFile": "NOPLoggerFactory.java"} -->NOPLoggerFactory is an trivial implementation of {@link
        ILoggerFactory} which always returns the unique instance of
        NOPLogger.
        @author Ceki G&uuml;lc&uuml;

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        */<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        package org.slf4j.helpers;
        import org.slf4j.ILoggerFactory;
        import org.slf4j.Logger;
        import org.slf4j.helpers.NOPLogger;
        /**
        NOPLoggerFactory is an trivial implementation of {@link
        ILoggerFactory} which always returns the unique instance of
        NOPLogger.
        @author Ceki G&uuml;lc&uuml;
        */
        public class NOPLoggerFactory implements ILoggerFactory {
        public NOPLoggerFactory() {
        // nothing to do
        }
        public Logger getLogger(String name) {
        return NOPLogger.NOP_LOGGER;
        }
        }
        (NOPLoggerFactory.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        <!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        /**
        The org.slf4j.Logger interface is the main user entry point of SLF4J API.
        It is expected that logging takes place through concrete implementations
        of this interface.
        Typical usage pattern:
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        public class Wombat {
        <span style="color:green">final static Logger logger = LoggerFactory.getLogger(Wombat.class);
        Integer t;
        Integer oldT;
        public void setTemperature(Integer temperature) {
        oldT = t;
        t = temperature;
        <span style="color:green">logger.debug("Temperature set to {}. Old temperature was {}.", t, oldT);
        if(temperature.intValue() > 50) {
        <span style="color:green">logger.info("Temperature has risen above 50 degrees.");
        }
        }
        }
        Be sure to read the FAQ entry relating to <a href="../../../faq.html#logging_performance">parameterized
        logging. Note that logging statements can be parameterized in
        <a href="../../../faq.html#paramException">presence of an exception/throwable.
        Once you are comfortable using loggers, i.e. instances of this interface, consider using
        <a href="MDC.html">MDC as well as <a href="Marker.html">Markers.
        @author Ceki G&uuml;lc&uuml;
        */
        public interface Logger {
        /**
        Case insensitive String constant used to retrieve the name of the root logger.
        @since 1.3
        */
        public final String ROOT_LOGGER_NAME = "ROOT";
        /**
        Return the name of this Logger instance.
        @return name of this logger instance
        */
        public String getName();
        /**
        Is the logger instance enabled for the TRACE level?
        @return True if this Logger is enabled for the TRACE level,
        false otherwise.
        @since 1.4
        */
        public boolean isTraceEnabled();
        /**
        Log a message at the TRACE level.
        @param msg the message string to be logged
        @since 1.4
        */
        public void trace(String msg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the TRACE level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the TRACE level.
        @param format the format string
        @param arg    the argument
        @since 1.4<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void trace(String format, Object arg);
        /**
        Log a message at the TRACE level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the TRACE level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        @since 1.4
        */
        public void trace(String format, Object arg1, Object arg2);
        /**
        Log a message at the TRACE level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the TRACE level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for TRACE. The variants taking #trace(String, Object) one and
        #trace(String, Object, Object) two arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments
        @since 1.4
        */
        public void trace(String format, Object... arguments);
        /**
        Log an exception (throwable) at the TRACE level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        @since 1.4
        */
        public void trace(String msg, Throwable t);
        /**
        Similar to #isTraceEnabled() method except that the
        marker data is also taken into account.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the TRACE level,
        false otherwise.
        @since 1.4
        */
        public boolean isTraceEnabled(Marker marker);
        /**
        <!-- e5db5ac6-1796-11ea-84d9-333445793454 <=< ACCEPT -->Log a message with the specific Marker at the TRACE level.
        @param marker the marker data specific to this log statement
        @param msg    the message string to be logged
        @since 1.4<!-- ACCEPT >=> e5db5ac6-1796-11ea-84d9-333445793454 -->
        */
        public void trace(Marker marker, String msg);
        /**
        This method is similar to #trace(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        @since 1.4
        */
        public void trace(Marker marker, String format, Object arg);
        /**
        This method is similar to #trace(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        @since 1.4
        */
        public void trace(Marker marker, String format, Object arg1, Object arg2);
        /**
        This method is similar to #trace(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker   the marker data specific to this log statement
        @param format   the format string
        @param argArray an array of arguments
        @since 1.4
        */
        public void trace(Marker marker, String format, Object... argArray);
        /**
        This method is similar to #trace(String, Throwable) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        @since 1.4
        */
        public void trace(Marker marker, String msg, Throwable t);
        /**
        Is the logger instance enabled for the DEBUG level?
        @return True if this Logger is enabled for the DEBUG level,
        false otherwise.
        */
        public boolean isDebugEnabled();
        /**
        Log a message at the DEBUG level.
        @param msg the message string to be logged
        */
        public void debug(String msg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the DEBUG level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the DEBUG level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void debug(String format, Object arg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the DEBUG level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the DEBUG level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void debug(String format, Object arg1, Object arg2);
        /**
        Log a message at the DEBUG level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the DEBUG level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for DEBUG. The variants taking
        #debug(String, Object) one and #debug(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void debug(String format, Object... arguments);
        /**
        Log an exception (throwable) at the DEBUG level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        */
        public void debug(String msg, Throwable t);
        /**
        Similar to #isDebugEnabled() method except that the
        marker data is also taken into account.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the DEBUG level,
        false otherwise.
        */
        public boolean isDebugEnabled(Marker marker);
        /**
        <!-- e5db5ac6-1796-11ea-84d9-333445793454 <=< ACCEPT -->Log a message with the specific Marker at the DEBUG level.
        @param marker the marker data specific to this log statement
        @param msg    the message string to be logged<!-- ACCEPT >=> e5db5ac6-1796-11ea-84d9-333445793454 -->
        */
        public void debug(Marker marker, String msg);
        /**
        This method is similar to #debug(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        */
        public void debug(Marker marker, String format, Object arg);
        /**
        This method is similar to #debug(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        */
        public void debug(Marker marker, String format, Object arg1, Object arg2);
        /**
        This method is similar to #debug(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void debug(Marker marker, String format, Object... arguments);
        /**
        This method is similar to #debug(String, Throwable) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        */
        public void debug(Marker marker, String msg, Throwable t);
        /**
        Is the logger instance enabled for the INFO level?
        @return True if this Logger is enabled for the INFO level,
        false otherwise.
        */
        public boolean isInfoEnabled();
        /**
        Log a message at the INFO level.
        @param msg the message string to be logged
        */
        public void info(String msg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the INFO level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the INFO level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void info(String format, Object arg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the INFO level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the INFO level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void info(String format, Object arg1, Object arg2);
        /**
        Log a message at the INFO level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the INFO level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for INFO. The variants taking
        #info(String, Object) one and #info(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void info(String format, Object... arguments);
        /**
        Log an exception (throwable) at the INFO level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        */
        public void info(String msg, Throwable t);
        /**
        Similar to #isInfoEnabled() method except that the marker
        data is also taken into consideration.
        @param marker The marker data to take into consideration
        @return true if this logger is warn enabled, false otherwise
        */
        public boolean isInfoEnabled(Marker marker);
        /**
        Log a message with the specific Marker at the INFO level.
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged
        */
        public void info(Marker marker, String msg);
        /**
        This method is similar to #info(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        */
        public void info(Marker marker, String format, Object arg);
        /**
        This method is similar to #info(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        */
        public void info(Marker marker, String format, Object arg1, Object arg2);
        /**
        This method is similar to #info(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void info(Marker marker, String format, Object... arguments);
        /**
        This method is similar to #info(String, Throwable) method
        except that the marker data is also taken into consideration.
        @param marker the marker data for this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        */
        public void info(Marker marker, String msg, Throwable t);
        /**
        Is the logger instance enabled for the WARN level?
        @return True if this Logger is enabled for the WARN level,
        false otherwise.
        */
        public boolean isWarnEnabled();
        /**
        Log a message at the WARN level.
        @param msg the message string to be logged
        */
        public void warn(String msg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the WARN level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the WARN level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void warn(String format, Object arg);
        /**
        Log a message at the WARN level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the WARN level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for WARN. The variants taking
        #warn(String, Object) one and #warn(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void warn(String format, Object... arguments);
        /**
        Log a message at the WARN level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the WARN level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        */
        public void warn(String format, Object arg1, Object arg2);
        /**
        Log an exception (throwable) at the WARN level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        */
        public void warn(String msg, Throwable t);
        /**
        Similar to #isWarnEnabled() method except that the marker
        data is also taken into consideration.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the WARN level,
        false otherwise.
        */
        public boolean isWarnEnabled(Marker marker);
        /**
        Log a message with the specific Marker at the WARN level.
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged
        */
        public void warn(Marker marker, String msg);
        /**
        This method is similar to #warn(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        */
        public void warn(Marker marker, String format, Object arg);
        /**
        This method is similar to #warn(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        */
        public void warn(Marker marker, String format, Object arg1, Object arg2);
        /**
        This method is similar to #warn(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void warn(Marker marker, String format, Object... arguments);
        /**
        This method is similar to #warn(String, Throwable) method
        except that the marker data is also taken into consideration.
        @param marker the marker data for this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        */
        public void warn(Marker marker, String msg, Throwable t);
        /**
        Is the logger instance enabled for the ERROR level?
        @return True if this Logger is enabled for the ERROR level,
        false otherwise.
        */
        public boolean isErrorEnabled();
        /**
        Log a message at the ERROR level.
        @param msg the message string to be logged
        */
        public void error(String msg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the ERROR level according to the specified format
        and argument.
        This form avoids superfluous object creation when the logger
        is disabled for the ERROR level.
        @param format the format string
        @param arg    the argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void error(String format, Object arg);
        /**
        <!-- 3566336e-1794-11ea-b389-333445793454 <=< ACCEPT -->Log a message at the ERROR level according to the specified format
        and arguments.
        This form avoids superfluous object creation when the logger
        is disabled for the ERROR level.
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument<!-- ACCEPT >=> 3566336e-1794-11ea-b389-333445793454 -->
        */
        public void error(String format, Object arg1, Object arg2);
        /**
        Log a message at the ERROR level according to the specified format
        and arguments.
        This form avoids superfluous string concatenation when the logger
        is disabled for the ERROR level. However, this variant incurs the hidden
        (and relatively small) cost of creating an Object[] before invoking the method,
        even if this logger is disabled for ERROR. The variants taking
        #error(String, Object) one and #error(String, Object, Object) two
        arguments exist solely in order to avoid this hidden cost.
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void error(String format, Object... arguments);
        /**
        Log an exception (throwable) at the ERROR level with an
        accompanying message.
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        */
        public void error(String msg, Throwable t);
        /**
        Similar to #isErrorEnabled() method except that the
        marker data is also taken into consideration.
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the ERROR level,
        false otherwise.
        */
        public boolean isErrorEnabled(Marker marker);
        /**
        Log a message with the specific Marker at the ERROR level.
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged
        */
        public void error(Marker marker, String msg);
        /**
        This method is similar to #error(String, Object) method except that the
        marker data is also taken into consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        */
        public void error(Marker marker, String format, Object arg);
        /**
        This method is similar to #error(String, Object, Object)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        */
        public void error(Marker marker, String format, Object arg1, Object arg2);
        /**
        This method is similar to #error(String, Object...)
        method except that the marker data is also taken into
        consideration.
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments
        */
        public void error(Marker marker, String format, Object... arguments);
        /**
        This method is similar to #error(String, Throwable)
        method except that the marker data is also taken into
        consideration.
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        */
        public void error(Marker marker, String msg, Throwable t);
        }
        (Logger.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

# File: `Marker.java`

## Method: `public void add(Marker reference)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(Marker reference)", "entityFile": "Marker.java"} -->Add a reference to another Marker.
        @param reference
        a reference to another marker
        @throws IllegalArgumentException
        if 'reference' is null

## Method: `public boolean remove(Marker reference)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean remove(Marker reference)", "entityFile": "Marker.java"} -->Remove a marker reference.
        @param reference
        the marker reference to remove
        @return true if reference could be found and removed, false otherwise.

## Method: `public boolean hasReferences()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean hasReferences()", "entityFile": "Marker.java"} -->Does this marker have any references?
        @return true if this marker has one or more references, false otherwise.

## Method: `public Iterator<Marker> iterator()`

        <!-- META {"entityType": "Method", "entitySignature": "public Iterator<Marker> iterator()", "entityFile": "Marker.java"} -->Returns an Iterator which can be used to iterate over the references of this
        marker. An empty iterator is returned when this marker has no references.
        @return Iterator over the references of this marker

## Method: `public boolean contains(Marker other)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean contains(Marker other)", "entityFile": "Marker.java"} -->Does this marker contain a reference to the 'other' marker? Marker A is defined
        to contain marker B, if A == B or if B is referenced by A, or if B is referenced
        by any one of A's references (recursively).
        @param other
        The marker to test for inclusion.
        @throws IllegalArgumentException
        if 'other' is null
        @return Whether this marker contains the other marker.

## Method: `public boolean contains(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean contains(String name)", "entityFile": "Marker.java"} -->Does this marker contain the marker named 'name'?
        If 'name' is null the returned value is always false.
        @param name The marker name to test for inclusion.
        @return Whether this marker contains the other marker.

## Method: `public boolean equals(Object o)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean equals(Object o)", "entityFile": "Marker.java"} -->Markers are considered equal if they have the same name.
        @param o
        @return true, if this.name equals o.name
        @since 1.5.1

## Method: `public int hashCode()`

        <!-- META {"entityType": "Method", "entitySignature": "public int hashCode()", "entityFile": "Marker.java"} -->Compute the hash code based on the name of this marker.
        Note that markers are considered equal if they have the same name.
        @return the computed hashCode
        @since 1.5.1

## Interface: `Marker`

        <!-- META {"entityType": "Interface", "entitySignature": "Marker", "entityFile": "Marker.java"} --><!-- 47b7c210-1797-11ea-932b-333445793454 <=< ACCEPT -->Markers are named objects used to enrich log statements. Conforming logging
        system Implementations of SLF4J determine how information conveyed by markers
        are used, if at all. In particular, many conforming logging systems ignore
        marker data.
        Markers can contain references to other markers, which in turn may contain
        references of their own.
        @author Ceki G&uuml;lc&uuml;<!-- ACCEPT >=> 47b7c210-1797-11ea-932b-333445793454 -->

# File: `None`

## None: `None`

        <!-- META {} --><!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->
        */
        package org.slf4j;
        import java.io.Serializable;
        import java.util.Iterator;
        /**
        <!-- 47b7c210-1797-11ea-932b-333445793454 <=< ACCEPT -->Markers are named objects used to enrich log statements. Conforming logging
        system Implementations of SLF4J determine how information conveyed by markers
        are used, if at all. In particular, many conforming logging systems ignore
        marker data.
        Markers can contain references to other markers, which in turn may contain
        references of their own.
        @author Ceki G&uuml;lc&uuml;<!-- ACCEPT >=> 47b7c210-1797-11ea-932b-333445793454 -->
        */
        public interface Marker extends Serializable {
        /**
        This constant represents any marker, including a null marker.
        */
        public final String ANY_MARKER = "*";
        /**
        This constant represents any non-null marker.
        */
        public final String ANY_NON_NULL_MARKER = "+";
        /**
        Get the name of this Marker.
        @return name of marker
        */
        public String getName();
        /**
        Add a reference to another Marker.
        @param reference
        a reference to another marker
        @throws IllegalArgumentException
        if 'reference' is null
        */
        public void add(Marker reference);
        /**
        Remove a marker reference.
        @param reference
        the marker reference to remove
        @return true if reference could be found and removed, false otherwise.
        */
        public boolean remove(Marker reference);
        /**
        @deprecated Replaced by #hasReferences().
        */
        public boolean hasChildren();
        /**
        Does this marker have any references?
        @return true if this marker has one or more references, false otherwise.
        */
        public boolean hasReferences();
        /**
        Returns an Iterator which can be used to iterate over the references of this
        marker. An empty iterator is returned when this marker has no references.
        @return Iterator over the references of this marker
        */
        public Iterator<Marker> iterator();
        /**
        Does this marker contain a reference to the 'other' marker? Marker A is defined
        to contain marker B, if A == B or if B is referenced by A, or if B is referenced
        by any one of A's references (recursively).
        @param other
        The marker to test for inclusion.
        @throws IllegalArgumentException
        if 'other' is null
        @return Whether this marker contains the other marker.
        */
        public boolean contains(Marker other);
        /**
        Does this marker contain the marker named 'name'?
        If 'name' is null the returned value is always false.
        @param name The marker name to test for inclusion.
        @return Whether this marker contains the other marker.
        */
        public boolean contains(String name);
        /**
        Markers are considered equal if they have the same name.
        @param o
        @return true, if this.name equals o.name
        @since 1.5.1
        */
        public boolean equals(Object o);
        /**
        Compute the hash code based on the name of this marker.
        Note that markers are considered equal if they have the same name.
        @return the computed hashCode
        @since 1.5.1
        */
        public int hashCode();
        }
        (Marker.java)
        <!-- 5a474d24-1791-11ea-9334-333445793454 <=< IGNORE -->Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<!-- IGNORE >=> 5a474d24-1791-11ea-9334-333445793454 -->

